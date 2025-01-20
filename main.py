import dash
import dash_cytoscape as cyto
from dash import html, dcc
from dash.dependencies import Input, Output
import networkx as nx

def create_realistic_graph():
    G = nx.DiGraph()

    companies = {
        "Google": {
            "CEO": ["Sundar Pichai"],
            "Industry": ["Technology", "Internet", "Artificial Intelligence"],
            "Products": ["Search Engine", "Cloud Platform", "Pixel Phones", "Chromecast"],
            "Services": ["Online Advertising", "Gmail", "Google Maps", "YouTube Premium"],
            "Competitors": ["Microsoft", "Amazon", "Meta", "Apple"],
            "Subsidiaries": ["YouTube", "DeepMind", "Fitbit"]
        },
        "Amazon": {
            "CEO": ["Andy Jassy"],
            "Industry": ["E-Commerce", "Cloud Computing", "Retail"],
            "Products": ["Kindle", "Fire TV", "Amazon Echo"],
            "Services": ["AWS", "Prime Video", "Amazon Music", "Fulfillment Services"],
            "Competitors": ["Google", "Microsoft", "eBay", "Alibaba"],
            "Subsidiaries": ["Whole Foods", "Zappos", "Ring"]
        },
        "Apple": {
            "CEO": ["Tim Cook"],
            "Industry": ["Technology", "Consumer Electronics"],
            "Products": ["iPhone", "MacBook", "iPad", "Apple Watch"],
            "Services": ["iCloud", "Apple Music", "Apple TV+", "App Store"],
            "Competitors": ["Microsoft", "Samsung", "Google", "Huawei"],
            "Subsidiaries": ["Beats Electronics", "Shazam"]
        },
        "Microsoft": {
            "CEO": ["Satya Nadella"],
            "Industry": ["Technology", "Software Development"],
            "Products": ["Windows OS", "Xbox", "Surface", "Microsoft 365"],
            "Services": ["Azure Cloud", "LinkedIn Learning", "GitHub Actions"],
            "Competitors": ["Google", "Apple", "Amazon", "IBM"],
            "Subsidiaries": ["LinkedIn", "GitHub", "Skype"]
        },
        "Meta": {
            "CEO": ["Mark Zuckerberg"],
            "Industry": ["Social Media", "Virtual Reality", "Advertising"],
            "Products": ["Facebook Platform", "Oculus VR", "Portal Devices"],
            "Services": ["Instagram Ads", "Messenger", "Facebook Gaming", "Workplace"],
            "Competitors": ["Google", "TikTok", "Snapchat", "Twitter"],
            "Subsidiaries": ["WhatsApp", "Instagram"]
        },
        "Tesla": {
            "CEO": ["Elon Musk"],
            "Industry": ["Automotive", "Clean Energy"],
            "Products": ["Model S", "Model X", "Model 3", "Model Y"],
            "Services": ["Supercharger Network", "Tesla Insurance", "Tesla Energy"],
            "Competitors": ["Ford", "Toyota", "Lucid Motors", "Rivian"],
            "Subsidiaries": ["SolarCity", "Tesla Grohmann Automation"]
        },
        "IBM": {
            "CEO": ["Arvind Krishna"],
            "Industry": ["Technology", "Consulting"],
            "Products": ["Mainframes", "IBM Power Systems", "Quantum Computers"],
            "Services": ["Cloud Computing", "IBM Watson AI", "Blockchain Services"],
            "Competitors": ["Microsoft", "Oracle", "Accenture", "Amazon"],
            "Subsidiaries": ["Red Hat", "Turbonomic"]
        },
        "Oracle": {
            "CEO": ["Safra Catz"],
            "Industry": ["Technology", "Database Software"],
            "Products": ["Oracle Database", "Java", "MySQL"],
            "Services": ["Cloud Infrastructure", "Consulting", "Oracle Support"],
            "Competitors": ["IBM", "Microsoft", "SAP", "Salesforce"],
            "Subsidiaries": ["NetSuite", "Cerner"]
        },
        "Samsung": {
            "CEO": ["Jong-Hee Han"],
            "Industry": ["Electronics", "Semiconductors", "Home Appliances"],
            "Products": ["Galaxy Smartphones", "Smart TVs", "Memory Chips"],
            "Services": ["Samsung Pay", "Samsung Health", "Bixby"],
            "Competitors": ["Apple", "Xiaomi", "Huawei", "LG"],
            "Subsidiaries": ["Harman International", "Samsung SDS", "Samsung Display"]
        },
        "Netflix": {
            "CEO": ["Ted Sarandos"],
            "Industry": ["Entertainment", "Streaming Media"],
            "Products": ["Netflix Originals", "Documentaries", "Stand-Up Specials"],
            "Services": ["Streaming Subscription", "DVD Rental", "Mobile Games"],
            "Competitors": ["Amazon Prime Video", "Disney+", "HBO Max", "Hulu"],
            "Subsidiaries": []
        },
        "Zoom": {
            "CEO": ["Eric Yuan"],
            "Industry": ["Communication Technology", "Video Conferencing"],
            "Products": ["Zoom Meetings", "Zoom Rooms", "Zoom Phone"],
            "Services": ["Webinars", "Virtual Events", "Zoom Marketplace"],
            "Competitors": ["Microsoft Teams", "Google Meet", "Cisco Webex", "BlueJeans"],
            "Subsidiaries": []
        },
        "Intel": {
            "CEO": ["Pat Gelsinger"],
            "Industry": ["Semiconductor", "Computer Hardware"],
            "Products": ["Core Processors", "Xeon", "Intel Arc GPUs"],
            "Services": ["AI Development", "Manufacturing Services", "IoT Solutions"],
            "Competitors": ["AMD", "NVIDIA", "Qualcomm"],
            "Subsidiaries": ["Mobileye", "Altera"]
        },
        "NVIDIA": {
            "CEO": ["Jensen Huang"],
            "Industry": ["Semiconductor", "AI Computing"],
            "Products": ["GeForce GPUs", "Tegra SOC", "NVIDIA RTX"],
            "Services": ["AI Platforms", "Supercomputing", "Cloud Gaming (GeForce NOW)"],
            "Competitors": ["AMD", "Intel", "Qualcomm"],
            "Subsidiaries": ["Mellanox", "Arm (Proposed Acquisition – later withdrawn)"]
        },
        "Adobe": {
            "CEO": ["Shantanu Narayen"],
            "Industry": ["Software", "Creative Tools"],
            "Products": ["Photoshop", "Illustrator", "Acrobat", "Lightroom"],
            "Services": ["Creative Cloud", "Document Cloud", "Adobe Stock", "Adobe Fonts"],
            "Competitors": ["Corel", "Canva", "Affinity", "Microsoft Publisher"],
            "Subsidiaries": ["Magento", "Marketo", "Behance"]
        },
        "SpaceX": {
            "CEO": ["Elon Musk"],
            "Industry": ["Aerospace", "Space Exploration"],
            "Products": ["Falcon 9", "Starship", "Dragon Capsule"],
            "Services": ["Satellite Launch", "Starlink Internet", "Rideshare Missions"],
            "Competitors": ["Blue Origin", "ULA", "Rocket Lab"],
            "Subsidiaries": []
        },
        "Uber": {
            "CEO": ["Dara Khosrowshahi"],
            "Industry": ["Transportation", "Tech Services"],
            "Products": ["Uber Rides", "Uber Freight", "Uber Reserve"],
            "Services": ["Uber Eats", "Uber for Business", "Uber Health"],
            "Competitors": ["Lyft", "Bolt", "Grab", "DiDi"],
            "Subsidiaries": ["Careem", "Postmates"]
        },
        "Airbnb": {
            "CEO": ["Brian Chesky"],
            "Industry": ["Hospitality", "Travel"],
            "Products": ["Vacation Rentals", "Experiences", "Airbnb Plus"],
            "Services": ["Host Tools", "Payment Processing", "AirCover (Insurance)"],
            "Competitors": ["VRBO", "Booking.com", "Expedia", "HomeAway"],
            "Subsidiaries": []
        },
        "Spotify": {
            "CEO": ["Daniel Ek"],
            "Industry": ["Music Streaming", "Technology"],
            "Products": ["Spotify App", "Spotify Kids", "Spotify Live"],
            "Services": ["Podcast Hosting", "Music Distribution", "Artist Analytics"],
            "Competitors": ["Apple Music", "Amazon Music", "YouTube Music", "Tidal"],
            "Subsidiaries": ["Megaphone", "Anchor"]
        },
        "Stripe": {
            "CEO": ["Patrick Collison"],
            "Industry": ["Fintech", "Online Payments"],
            "Products": ["Payment Gateway", "Stripe Terminal", "Billing"],
            "Services": ["Subscription Management", "Fraud Prevention", "Stripe Atlas"],
            "Competitors": ["PayPal", "Adyen", "Square", "Braintree"],
            "Subsidiaries": []
        },
        "Lyft": {
            "CEO": ["David Risher"],
            "Industry": ["Transportation", "Mobility"],
            "Products": ["Lyft Rides", "Lyft Bikes", "Lyft Scooters"],
            "Services": ["Lyft Business", "Scooter Rentals", "Car Rentals"],
            "Competitors": ["Uber", "Via", "Bolt", "Gett"],
            "Subsidiaries": []
        },
        "TikTok": {
            "CEO": ["Shou Zi Chew"],
            "Industry": ["Social Media", "Entertainment"],
            "Products": ["Video Creation Tools", "TikTok LIVE", "TikTok Shop"],
            "Services": ["Content Monetization", "Advertising", "Creator Marketplace"],
            "Competitors": ["Meta", "Snapchat", "YouTube", "Kuaishou"],
            "Subsidiaries": []
        },
        "PayPal": {
            "CEO": ["Dan Schulman"],
            "Industry": ["Fintech", "Online Payments"],
            "Products": ["PayPal Wallet", "PayPal Credit", "Pay in 4"],
            "Services": ["Peer-to-Peer Payments", "Payment Processing", "Braintree"],
            "Competitors": ["Stripe", "Square", "Skrill", "Authorize.Net"],
            "Subsidiaries": ["Venmo", "Honey"]
        },
        "Snapchat": {
            "CEO": ["Evan Spiegel"],
            "Industry": ["Social Media", "Camera Technology"],
            "Products": ["Snap Camera", "Spectacles", "Snap Minis"],
            "Services": ["Advertising", "Snapchat Discover", "Spotlight"],
            "Competitors": ["TikTok", "Meta", "Pinterest", "YouTube Shorts"],
            "Subsidiaries": []
        },
        "Pinterest": {
            "CEO": ["Bill Ready"],
            "Industry": ["Social Media", "Discovery Platform"],
            "Products": ["Idea Pins", "Pinterest Boards", "Pinterest Lens"],
            "Services": ["Advertising", "Shopping Features", "Creator Rewards"],
            "Competitors": ["Instagram", "TikTok", "Snapchat", "Etsy (marketplace)"],
            "Subsidiaries": []
        },
        "Dell": {
            "CEO": ["Michael Dell"],
            "Industry": ["Technology", "Computer Hardware"],
            "Products": ["XPS Laptops", "PowerEdge Servers", "Monitors", "Alienware PCs"],
            "Services": ["IT Solutions", "Dell Financial Services", "SupportAssist"],
            "Competitors": ["HP", "Lenovo", "Acer", "Asus"],
            "Subsidiaries": ["Alienware", "VMware (Majority Stake Sold in 2021)"]
        },
        "Cisco": {
            "CEO": ["Chuck Robbins"],
            "Industry": ["Networking", "Telecommunications"],
            "Products": ["Routers", "Switches", "Cisco Webex Devices"],
            "Services": ["Cybersecurity", "Collaboration Tools", "Managed Services"],
            "Competitors": ["Juniper Networks", "Huawei", "Aruba (HPE)", "Avaya"],
            "Subsidiaries": ["AppDynamics", "Meraki", "OpenDNS"]
        },
        "Shopify": {
            "CEO": ["Tobi Lütke"],
            "Industry": ["E-Commerce", "SaaS"],
            "Products": ["Online Store Builder", "Shopify POS", "Shopify App Store"],
            "Services": ["Subscription Management", "Payments", "Fulfillment Network"],
            "Competitors": ["WooCommerce", "BigCommerce", "Wix", "Squarespace"],
            "Subsidiaries": ["Oberlo (Discontinued)", "Handshake"]
        },
        "Cloudflare": {
            "CEO": ["Matthew Prince"],
            "Industry": ["Cloud Services", "Cybersecurity"],
            "Products": ["CDN", "DNS Resolver", "Load Balancer"],
            "Services": ["DDoS Protection", "Zero Trust Security", "Serverless Platform"],
            "Competitors": ["Akamai", "Fastly", "Amazon CloudFront", "Imperva"],
            "Subsidiaries": []
        },
        "Salesforce": {
            "CEO": ["Marc Benioff"],
            "Industry": ["Cloud Software", "Enterprise Software"],
            "Products": ["Sales Cloud", "Marketing Cloud", "Tableau", "Slack"],
            "Services": ["Customer Support", "Analytics", "CRM Integration"],
            "Competitors": ["Oracle", "Microsoft", "SAP", "Adobe"],
            "Subsidiaries": ["Tableau", "Slack", "MuleSoft"]
        },
        "Toyota": {
            "CEO": ["Koji Sato"],
            "Industry": ["Automotive", "Mobility"],
            "Products": ["Hybrid Vehicles", "Fuel Cell Cars", "Toyota Supra"],
            "Services": ["Mobility Solutions", "Toyota Financial Services", "Car Sharing"],
            "Competitors": ["Ford", "Volkswagen", "Honda", "GM"],
            "Subsidiaries": ["Daihatsu", "Hino Motors"]
        },
        "Ford": {
            "CEO": ["Jim Farley"],
            "Industry": ["Automotive"],
            "Products": ["Electric Vehicles", "Trucks", "Mustang", "Ford GT"],
            "Services": ["Fleet Management", "Ford Credit", "FordPass"],
            "Competitors": ["Toyota", "GM", "Tesla", "Honda"],
            "Subsidiaries": []
        }
    }
    for company, data in companies.items():
        # Attach list attributes to the company node
        G.add_node(
            company,
            type="company",
            industry=data["Industry"],
            Products=data["Products"],
            Services=data["Services"],
            Competitors=data["Competitors"],
            Subsidiaries=data["Subsidiaries"]
        )

        # CEO(s)
        for ceo in data["CEO"]:
            G.add_node(ceo, type="person")
            G.add_edge(ceo, company, relation="CEO of")

        # Product, service, subsidiary nodes
        for product in data["Products"]:
            n = f"{company} - {product}"
            G.add_node(n, type="product")
            G.add_edge(company, n, relation="produces")

        for serv in data["Services"]:
            n = f"{company} - {serv}"
            G.add_node(n, type="service")
            G.add_edge(company, n, relation="offers")

        for competitor in data["Competitors"]:
            # "competes with" edge
            G.add_edge(company, competitor, relation="competes with")

        for sub in data["Subsidiaries"]:
            G.add_node(sub, type="subsidiary")
            G.add_edge(company, sub, relation="owns")

    return G

# Build the graph
realistic_graph = create_realistic_graph()

# Prebuild the “full” elements in case we need to reset/show everything
full_elements = []
for node, data in realistic_graph.nodes(data=True):
    full_elements.append({
        "data": {
            "id": node,
            "label": node,
            "type": data.get("type", "unknown"),
            "industry": data.get("industry", [])
        }
    })
for source, target, data in realistic_graph.edges(data=True):
    full_elements.append({
        "data": {
            "source": source,
            "target": target,
            "label": data.get("relation", "")
        }
    })

# Which attributes can we pick in the first dropdown?
groupable_attributes = ["industry", "type", "Products", "Services", "Competitors", "Subsidiaries"]

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H2("Enhanced Realistic Knowledge Graph Visualization", style={"textAlign": "center"}),
    html.Div("Legend: Blue - Company, Green - Product, Orange - Service, Purple - Person, Yellow - Subsidiary",
             style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div([
        html.Label("Group by Attribute:"),
        dcc.Dropdown(
            id='grouping-attribute-dropdown',
            options=[{'label': attr, 'value': attr} for attr in groupable_attributes],
            value=None,
            placeholder="Select an attribute"
        ),
    ], style={"width": "50%", "margin": "0 auto 20px"}),

    html.Div([
        html.Label("Select Value:"),
        dcc.Dropdown(
            id='grouping-value-dropdown',
            placeholder="Select a value",
            disabled=True
        ),
    ], style={"width": "50%", "margin": "0 auto 20px"}),

    html.Div(
        html.Button("Reset Filters", id="reset-button", n_clicks=0),
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    cyto.Cytoscape(
        id='cytoscape',
        elements=full_elements,  # Start unfiltered
        layout={
            "name": "cose",
            "animate": True,
            "nodeRepulsion": 1500000,
            "gravity": 0.2,
            "numIter": 1500
        },
        style={"width": "100%", "height": "1000px"},
        stylesheet=[
            {"selector": 'node[type="company"]',
             "style": {"background-color": "blue", "label": "data(label)",
                       "width": 50, "height": 50}},
            {"selector": 'node[type="product"]',
             "style": {"background-color": "green", "label": "data(label)",
                       "width": 40, "height": 40}},
            {"selector": 'node[type="service"]',
             "style": {"background-color": "orange", "label": "data(label)",
                       "width": 40, "height": 40}},
            {"selector": 'node[type="person"]',
             "style": {"background-color": "purple", "label": "data(label)",
                       "width": 35, "height": 35}},
            {"selector": 'node[type="subsidiary"]',
             "style": {"background-color": "yellow", "label": "data(label)",
                       "width": 35, "height": 35}},
            {"selector": 'edge[label="CEO of"]',
             "style": {"line-color": "#FF5733", "width": 3,
                       "label": "data(label)", "font-size": 12}},
            {"selector": 'edge[label="produces"]',
             "style": {"line-color": "#33FF57", "width": 3,
                       "label": "data(label)", "font-size": 12}},
            {"selector": 'edge[label="offers"]',
             "style": {"line-color": "#3385FF", "width": 3,
                       "label": "data(label)", "font-size": 12}},
            {"selector": 'edge[label="competes with"]',
             "style": {"line-color": "#FFC300", "width": 3,
                       "label": "data(label)", "font-size": 12}},
            {"selector": 'edge[label="owns"]',
             "style": {"line-color": "#FFD700", "width": 3,
                       "label": "data(label)", "font-size": 12}}
        ]
    )
])

@app.callback(
    Output('grouping-attribute-dropdown', 'value'),
    Output('grouping-value-dropdown', 'options'),
    Output('grouping-value-dropdown', 'disabled'),
    Output('grouping-value-dropdown', 'value'),
    Output('cytoscape', 'elements'),
    Input('grouping-attribute-dropdown', 'value'),
    Input('grouping-value-dropdown', 'value'),
    Input('reset-button', 'n_clicks')
)
def update_filters_and_graph(attribute, value, reset_clicks):
    """Single callback for building second-dropdown options,
       updating the graph, and resetting everything."""
    ctx = dash.callback_context
    if not ctx.triggered:
        # Page just loaded
        return attribute, [], True, None, full_elements

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # 1) If user clicked "Reset" -> show full graph, clear both dropdowns
    if triggered_id == 'reset-button':
        return None, [], True, None, full_elements

    # 2) If no attribute chosen -> second dropdown is blank & disabled, show full graph
    if not attribute:
        return None, [], True, None, full_elements

    # 3) Populate second dropdown with all distinct values for this attribute
    unique_values = set()
    for _, data in realistic_graph.nodes(data=True):
        attr_val = data.get(attribute, [])
        if isinstance(attr_val, list):
            unique_values.update(attr_val)
        elif attr_val is not None:
            unique_values.add(attr_val)
    dropdown_opts = [{'label': v, 'value': v} for v in sorted(unique_values)]

    # If no value chosen yet, just enable the second dropdown but show full graph
    if not value:
        return attribute, dropdown_opts, False, None, full_elements

    # 4) We have attribute + value -> find all nodes that contain that value
    matching_nodes = []
    for node, node_data in realistic_graph.nodes(data=True):
        node_attr_val = node_data.get(attribute, [])
        if isinstance(node_attr_val, list):
            if value in node_attr_val:
                matching_nodes.append(node)
        else:
            if node_attr_val == value:
                matching_nodes.append(node)

    # 5) From each matching node, do a BFS/DFS outward ignoring "competes with"
    keep_nodes = set()
    for start_node in matching_nodes:
        stack = [start_node]
        while stack:
            curr = stack.pop()
            if curr not in keep_nodes:
                keep_nodes.add(curr)
                # Explore neighbors, skipping "competes with" edges
                for neighbor in realistic_graph.neighbors(curr):
                    edge_data = realistic_graph[curr][neighbor]
                    relation = edge_data.get('relation', '')
                    # If you want to exclude "competes with" only, skip it:
                    if relation != 'competes with':
                        stack.append(neighbor)

    # 6) Build edges from the subgraph, skipping "competes with"
    filtered_edges = []
    for s, t, edge_data in realistic_graph.edges(data=True):
        if s in keep_nodes and t in keep_nodes:
            if edge_data.get("relation", "") != "competes with":
                filtered_edges.append({
                    "data": {
                        "source": s,
                        "target": t,
                        "label": edge_data.get("relation", "")
                    }
                })

    # 7) Build node elements from keep_nodes
    filtered_nodes = []
    for node_id in keep_nodes:
        node_data = realistic_graph.nodes[node_id]
        filtered_nodes.append({
            "data": {
                "id": node_id,
                "label": node_id,
                "type": node_data.get("type", "unknown"),
                "industry": node_data.get("industry", [])
            }
        })

    return attribute, dropdown_opts, False, value, filtered_edges + filtered_nodes

if __name__ == "__main__":
    app.run_server(debug=True)
