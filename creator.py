import json
import torch
from transformers import BertTokenizer, BertForTokenClassification
from transformers import pipeline
from flair.models import SequenceTagger
from flair.data import Sentence
from spacy import load as spacy_load
from nltk import pos_tag, word_tokenize
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from spacy.pipeline import EntityRuler
from gensim.models import KeyedVectors

# Load BERT-based model and tokenizer for Named Entity Recognition (NER)
bert_tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
bert_model = BertForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
bert_pipeline = pipeline("ner", model=bert_model, tokenizer=bert_tokenizer, aggregation_strategy="simple")

# Load Flair NER model for additional entity detection
flair_tagger = SequenceTagger.load("flair/ner-english")

# Load SpaCy model for linguistic processing and rule-based entity detection
spacy_nlp = spacy_load("en_core_web_sm")

# Add custom entity rules for SpaCy
entity_ruler = EntityRuler(spacy_nlp)
custom_rules = [
    {"label": "CEO", "pattern": [{"LOWER": "ceo"}]},
    {"label": "COMPETITOR", "pattern": [{"LOWER": "competitor"}]}
]
entity_ruler.add_patterns(custom_rules)
spacy_nlp.add_pipe(entity_ruler, before="ner")

# Load model for text summarization
summarizer_tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
summarizer_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

# Load pre-trained Word2Vec model for synonym matching (e.g., entity categorization)
word2vec_model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True, limit=100000)

# BERT NER extraction
def ner_with_bert(text):
    """Extract entities using BERT-based model."""
    return bert_pipeline(text)

# Flair NER extraction
def ner_with_flair(text):
    """Extract entities using Flair NER model."""
    sentence = Sentence(text)
    flair_tagger.predict(sentence)
    return [
        {'word': entity.text, 'entity_group': entity.tag, 'score': entity.score}
        for entity in sentence.get_spans('ner')
    ]

# SpaCy NER extraction
def ner_with_spacy(text):
    """Extract entities using SpaCy with custom rules."""
    doc = spacy_nlp(text)
    return [
        {'word': ent.text, 'entity_group': ent.label_, 'score': 1.0}  # SpaCy does not provide confidence scores
        for ent in doc.ents
    ]

# Extract noun phrases using NLTK
def extract_noun_phrases(text):
    """Extract noun phrases from text using part-of-speech tagging."""
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    return [word for word, pos in tagged if pos in ('NN', 'NNS', 'NNP', 'NNPS')]

# Preprocess text for clustering
def preprocess_text(text):
    """Clean text by removing special characters and converting to lowercase."""
    return re.sub(r'[^a-zA-Z0-9 ]', '', text).lower()

# Cluster text into topics using TF-IDF and KMeans
def cluster_text(texts, n_clusters=5):
    """Perform clustering on text to identify thematic groups."""
    preprocessed_texts = [preprocess_text(text) for text in texts]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(preprocessed_texts)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(tfidf_matrix)
    return kmeans.labels_

# Summarize text using BART model
def summarize_text(text):
    """Generate a summary for the given text."""
    inputs = summarizer_tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = summarizer_model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    return summarizer_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Merge results from multiple NER models with confidence filtering
def merge_ner_results(*ner_results, confidence_threshold=0.8):
    """Merge and filter entities from multiple NER models based on confidence scores."""
    merged_results = {}
    for result_set in ner_results:
        for entity in result_set:
            if entity['score'] >= confidence_threshold:
                key = entity['word']
                if key not in merged_results:
                    merged_results[key] = {
                        'entity_group': entity['entity_group'],
                        'score': entity['score']
                    }
                else:
                    merged_results[key]['score'] = max(merged_results[key]['score'], entity['score'])
    return merged_results

# Segment text into structured data
def segment_text(text):
    """Extract, categorize, and organize entities from the text."""
    bert_entities = ner_with_bert(text)
    flair_entities = ner_with_flair(text)
    spacy_entities = ner_with_spacy(text)
    noun_phrases = extract_noun_phrases(text)

    merged_entities = merge_ner_results(bert_entities, flair_entities, spacy_entities)

    segmented_data = defaultdict(lambda: {
        "CEO": [],
        "Industry": [],
        "Products": [],
        "Services": [],
        "Competitors": [],
        "Subsidiaries": []
    })

    # Categorize entities into predefined fields
    category_keywords = {
        "ceo": "CEO",
        "manager": "CEO",
        "industry": "Industry",
        "product": "Products"
    }

    for word, details in merged_entities.items():
        word = map_to_synonyms(word.lower(), category_keywords)
        entity_group = details['entity_group']
        if entity_group in ['ORG', 'GPE']:  # Organizations or locations as companies
            if word not in segmented_data:
                segmented_data[word]  # Initialize company structure
        elif entity_group == 'PERSON':
            for company in segmented_data:
                segmented_data[company]["CEO"].append(word)
        elif entity_group in ['MISC', 'NORP']:
            for company in segmented_data:
                segmented_data[company]["Industry"].append(word)
        elif entity_group == 'PRODUCT':
            for company in segmented_data:
                segmented_data[company]["Products"].append(word)

    for phrase in noun_phrases:
        for company in segmented_data:
            segmented_data[company]["Products"].append(phrase)

    # Add clustering and summarization results
    clusters = cluster_text([text])
    for idx, cluster in enumerate(clusters):
        segmented_data[f"Cluster_{cluster}"] = {
            "Summary": summarize_text(text.split('.')[idx].strip()) if idx < len(text.split('.')) else "",
        }

    return dict(segmented_data)

# Read the input text file
input_file = "big_text_file.txt"
with open(input_file, "r", encoding="utf-8") as file:
    big_text = file.read()

# Process and segment the text
segmented_data = segment_text(big_text)

# Save the structured data to a JSON file
output_file = "segmented_data.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(segmented_data, file, indent=4)

print(f"Segmented data has been saved to {output_file}")
