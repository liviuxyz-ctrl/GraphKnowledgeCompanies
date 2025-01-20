# GraphKnowledge Visualizer

## Overview
The GraphKnowledge Visualizer is a web-based application designed to visualize relationships and knowledge graphs using the Dash framework and Cytoscape. This tool represents entities (such as companies, products, services, and individuals) as nodes and their relationships (e.g., "CEO of", "produces", "competes with") as edges in an interactive graph.

---

## Features
- **Interactive Graph Visualization**: Explore relationships dynamically using Cytoscape.
- **Categorized Nodes**: Nodes are color-coded based on their type (e.g., company, product, service).
- **Filter and Group**: Users can group or filter nodes based on attributes like industry, type, or competitors.
- **Reset and Full View**: Easily reset filters to view the full graph.
- **Customizable Layouts**: Layouts can be updated for better visual clarity.

---

## How It Works
1. **Data Representation**: The relationships between entities are represented as nodes and edges using NetworkX.
2. **Graph Rendering**: The full graph is pre-rendered with attributes and styles for each node and edge.
3. **User Interaction**:
   - Users can select grouping attributes and filter values using dropdowns.
   - Reset filters to show the entire graph.
4. **Visualization**: Dash Cytoscape renders the graph interactively, allowing panning, zooming, and exploration.

---

## Key Node and Edge Types
### Node Types:
- **Company**: Blue nodes represent organizations.
- **Product**: Green nodes represent products created by companies.
- **Service**: Orange nodes represent services offered by companies.
- **Person**: Purple nodes represent individuals, such as CEOs.
- **Subsidiary**: Yellow nodes represent subsidiaries owned by companies.

### Edge Types:
- **CEO of**: Links individuals to their companies (red edges).
- **Produces**: Links companies to their products (green edges).
- **Offers**: Links companies to their services (blue edges).
- **Competes with**: Links competitors (yellow edges).
- **Owns**: Links companies to their subsidiaries (gold edges).

---

## Setup and Installation
### Prerequisites
- Python 3.7+
- Dash and its dependencies
- NetworkX

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/liviuxyz-ctrl/GraphKnowledgeCompanies/
   cd GraphKnowledgeCompanies
   ```
2. Install required Python libraries:
   ```bash
   pip install dash dash-cytoscape networkx
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:8050`.

---

## Example Visualization

![image](https://github.com/user-attachments/assets/cf841a9f-371b-4651-bef7-be53fcd3d2f6)


![image](https://github.com/user-attachments/assets/b1eac94a-3768-4ae2-ba34-b1ae4eaa6ccd)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

