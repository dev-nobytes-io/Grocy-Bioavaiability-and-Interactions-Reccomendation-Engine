> **Preserved original.** This is the project README as it stood on 26 September 2026, before the documentation phase. It is kept verbatim, including its formatting problems, as the record of the founding vision. The current entry point is the [top-level README](../../README.md). The [project brief](project-brief.md) assesses every claim below against the literature.

---

# Grocy-Bioavaiability-and-Interactions-Reccomendation-Engine
This takes in data from Grocy (your kitchen's management system) and medical data about bioavailability of nutrients amd their interaction with each other, and more to come to a reccomendation of a more effective meal plan for your goals.

It touches on the fields of Metabolomics and Nutrigenomics in its search to achieve specific biological health and fitness goals through additive nutrition and fitness. 


# ArcadeDB Use Cases

mindmap
  root((ArcadeDB Use Cases))
    ::icon(fa fa-database)
    AI and Semantic Operations
      Advanced GraphRAG
        Hybrid Context Engines
        Contextual LLM Memory
      Multimodal Recommendations
        Social E-commerce
        Content Personalisation
      Entity Resolution
        Data De-duplication
        Fuzzy Identity Matching
      Semantic Search
        Vector-Filtered Content
        Intent-Based Discovery
    Cybersecurity and Risk
      Fraud Ring Detection
        Circular Payment Tracking
        Shared Device Networks
      Enterprise IAM
        Hierarchical Permissions
        Role-Based Access (RBAC)
      Threat Intelligence
        Malware Vector Linkage
        Network Dependency Logs
    Network and Supply Chain
      Infrastructure Topology
        Microservices Telemetry
        Telecom Network Mapping
      Logistics Management
        Bill of Materials (BOM)
        Geospatial Fleet Routing
      Impact Analysis
        Cascade Failure Modeling
        Dependency Bottlenecks
    Unified Operational Systems
      Customer 360 View
        JSON Session Event Logs
        Relational Profile Merging
      High-Speed Caching
        Session State Storage
        Rapid Key-Value Lookups
      Location-Aware Apps
        Proximity Graph Searches
        Rideshare Dispatch Optimization


# The goal 

graph TD
    %% Styles and Themes
    classDef chaotic fill:#FFECEC,stroke:#FF8888,stroke-width:2px,stroke-dasharray: 5 5;
    classDef multiModel fill:#E6F0FA,stroke:#4A90E2,stroke-width:2px;
    classDef rigid fill:#E6F9EC,stroke:#2ECC71,stroke-width:2px;
    classDef validation fill:#FDF2E2,stroke:#F39C12,stroke-width:2px;
    classDef action fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px;

    %% 1. CHAOTIC FLUID INPUTS (The Unpredictable Reality)
    subgraph Chaotic_Inputs ["1. The Chaotic Fluid (Real-Time Inputs)"]
        User_State["Unstructured Input <br><i>'Slept poorly, fried CNS, leg day sore'</i>"]:::chaotic
        Kitchen_Inv["Kitchen & Grocery Inventory <br><i>(Dynamic Sub-Graph: What you own)</i>"]:::chaotic
        Environment["Unpredictable Environment <br><i>(Varying stress, context, moment-to-moment)</i>"]:::chaotic
    end

    %% 2. ARCADE DB MULTI-MODEL CORE
    subgraph Engine_Core ["2. ArcadeDB Multi-Model Core Engine"]
        Vector_Layer["<b>Vector Engine (Intent/State)</b><br>Encodes messy inputs into semantic 'State' coordinates<br><i>Matches 'Sore' to 'Recovery Pathways'</i>"]:::multiModel
        Doc_Store["<b>Document Store (Metadata)</b><br>Stores raw ingredient JSON data, recipe text, & dosages"]:::multiModel
        Graph_Layer["<b>Graph Engine (Entity Relationships)</b><br>Executes fast multi-hop traversals over interconnected nodes"]:::multiModel
    end

    %% 3. THE UNCHANGING ANCHOR (Rigid Biology)
    subgraph Rigid_Biology ["3. The Unchanging Anchor (Rigid Biology)"]
        Biochem_Laws["Immutable Biochemical Laws <br><i>(e.g., Vitamin C reduces Ferric Iron)</i>"]:::rigid
        Microbiome_Nodes["Microbiome Map <br><i>(Taxonomic strains & redundant metabolic pathways)</i>"]:::rigid
    end

    %% 4. THE POSITIVE HEALTH RECOMMENDATION ENGINE
    subgraph Positive_Engine ["4. Positive Health (Additive) Recommendation Engine"]
        Synergy_Calc["<b>Anabolic Synergy Index (ASI) Solver</b><br>Calculates compounding conditional scores (+Weights)"]:::action
        
        direction LR
        Rec_Unlock["<b>Additive Recommendation Output</b><br>👉 Keep eating your meal<br>👉 <b>ADD</b> Companion Pairs<br>👉 <i>(e.g., Squeeze Lemon, Add Black Pepper)</i>"]:::action
    end

    %% 5. OBJECTIVE VALIDATION LOOP
    subgraph Validation_Loop ["5. Objective Validation Layer"]
        User_Action["User Eats Meal Matrix <br><i>(Zero friction, additive optimization)</i>"]:::validation
        Blood_Panels["<b>Measurable Blood Biomarkers</b><br><i>(hs-CRP, Fasting Insulin, Creatine Kinase)</i>"]:::validation
    end

    %% DATA PIPELINE & EDGE RELATIONSHIPS
    User_State -->|Vector Embedding| Vector_Layer
    Environment -->|Shifts Vibe Coordinate| Vector_Layer
    Kitchen_Inv -->|Natively queries available nodes| Graph_Layer
    
    Vector_Layer -->|Pins target anchors on| Graph_Layer
    Doc_Store -->|Hydrates nodes with text/data| Graph_Layer
    
    Biochem_Laws -->|Establishes hard edges| Graph_Layer
    Microbiome_Nodes -->|Establishes functional paths| Graph_Layer
    
    Graph_Layer -->|Feeds structural paths to| Synergy_Calc
    Synergy_Calc -->|Generates positive action| Rec_Unlock
    
    Rec_Unlock -->|Guides| User_Action
    User_Action -->|Alters internal small-molecule metabolomics| Blood_Panels
    
    %% THE RECOVERY FEEDBACK LOOP
    Blood_Panels -->|Updates historical time-series sub-graph & recalibrates weights| Graph_Layer

    %% Legend Visual Anchors
    style Chaotic_Inputs fill:none,stroke:#FF8888,stroke-width:1px
    style Engine_Core fill:none,stroke:#4A90E2,stroke-width:1px
    style Rigid_Biology fill:none,stroke:#2ECC71,stroke-width:1px
    style Positive_Engine fill:none,stroke:#9C27B0,stroke-width:1px
    style Validation_Loop fill:none,stroke:#F39C12,stroke-width:1px

# Comprehensive Summary: Biocentric Recommendation Engine Architecture

This document provides a highly detailed engineering and philosophical summary of a next-generation **Hyper-Personalised Biocentric Recommendation Engine**. The platform leverages a multi-model database architecture (**ArcadeDB**) to map an "any-to-any" relational grid connecting human lifestyle, physical goals, blood biomarkers, gut microbiomes, and local grocery/kitchen inventories under a **Positive Health (Additive)** paradigm.

---

## 1. The Core Vision & Problem Statement

### The "Specificity Gap" in Modern Wellness
Traditional clinical and fitness advice peaks at generic blanket statements: *"Eat a balanced diet and get regular exercise."* While fundamentally true, this advice lacks personal specificity and actionability. Human biology is a chaotic, non-linear, and non-replicable systemâ€”unpredictable moment to moment, where a single night of poor sleep can completely alter metabolic and gut microbial realities.

### The Target Demographic Wedge
The platform initially anchors its value proposition on fitness enthusiasts ("gym rats"). This cohort possesses exceptional macro-discipline (counting protein, fats, and carbs down to the decimal point) but suffers from complete **micronutrient and bioavailability blindness**. They routinely mega-dose competing supplements, combine clashing food matrices that cause "anabolic waste," or experience broad-spectrum gut dysbiosis due to heavy protein/sweetener loads.

---

## 2. Core Architectural Pillars (The ArcadeDB Advantage)

To resolve the challenge of high-dimensional, fragmented data silos, the engine utilizes **ArcadeDB**, a multi-model database that combines a native Graph Engine, an LSM-powered Vector Search Engine, and a Document Store under a single ACID transaction boundary.

```
       [THE UNCHANGING ANCHOR]                 [THE CHAOTIC FLUID]
    Immutable Laws of Biochemistry        Fuzzy, Real-Time Human States
    (Mapped via Native Graph Nodes)    <==> (Mapped via Vector Embeddings)
```

1. **The Vector Layer (Intent & Semantic Smoothing):** Translates messy, unstructured human inputs (e.g., *"CNS fried, joints sore from squats"*) into mathematical coordinates. It bypasses rigid deterministic calculations in favour of *probabilistic trends*, mapping a user's momentary "vibe" to target biological recovery states.
2. **The Graph Layer (Biological Pathways):** Traverses the rigid, immutable laws of chemistry and taxonomic microbiology (e.g., how an ingredient transforms into a prebiotic, feeds a microbe, alters a hormone, or competes for an enterocyte transporter).
3. **The Document Layer (Metadata Storage):** Treats individual nodes as JSON documents. This allows dense, unstructured textual data (like clinical abstracts, recipe instructions, or ingredient profiles from FooDB) to sit right on the node without sacrificing index-free graph traversal speeds.

---

## 3. The Positive Health (Additive Nutrition) Philosophy

Rather than acting as a restrictive "food cop" that filters out hazards (e.g., *"Don't eat X"*), the engine functions as an **anabolic optimizer**. It focuses entirely on what the user can **add** to their current meal matrix to multiply performance, absorption, and recovery.

* **Bioavailability Unlock Keys (Companion Pairs):** The graph identifies synergistic biological relationships to create immediate, micro-additive actions based on what is true in the kitchen *right now*:
  * *Example:* Adding a squeeze of citrus (Vitamin C) to plant-based greens to chemically reduce ferric iron into highly absorbable ferrous iron, overriding native plant phytate inhibitors.
  * *Example:* Pairing black pepper (piperine) and fat with turmeric to boost curcumin bioavailability by up to 2,000%.
* **Microbial Feeding:** Scans the user's microbiome profile to find redundant metabolic pathways. If a primary strain is depleted, it recommends adding specific prebiotic fibres or polyphenols to feed surviving bacteria capable of synthesizing critical recovery compounds (like Urolithin A or short-chain fatty acids).

---

## 4. The Unified Cross-Domain "Any-to-Any" Data Map

Because standard biological databases are heavily siloed, the engine acts as an overarching semantic layout, weaving fragmented global standards together via their universal identifiers:

* **Nutrients & Compounds:** Sourced from **FooDB** & **ChEBI** *(Food Source $
ightarrow$ Chemical Structure)*.
* **Enzymes, Reactions & Pathways:** Sourced from **KEGG Pathways** & **Reactome** *(Compound $
ightarrow$ Enzyme $
ightarrow$ Metabolic Path)*.
* **Proteins & Amino Acids:** Sourced from **UniProt** *(Amino Acid Sequence $
ightarrow$ Functional Protein)*.
* **Hormones, Microbes & Behaviours:** Unified via the **Human Metabolome Database (HMDB)**, **Virtual Metabolic Human (VMH)**, and behavioral taxonomies like **MeSH Terms**.

---

## 5. The Measurable Validation Loop (The Blood Milestone)

The engine establishes a continuous, objective feedback mechanism using **sequential blood panel diagnostics (Metabolomics & Nutrigenomics)**. Blood biomarkers serve as the ultimate validation layer to prove whether a dietary recommendation successfully influenced the body.

```
[Engine Suggests Additive Multiplier] â”€â”€> [User Eats Combined Meal] â”€â”€> [Blood Panel Tracks Response]
                  ^                                                                  |
                  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€(Database Recalibrates Graph Weights)â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

The database maps actionable solutions directly to objective blood anomalies using an **Anabolic Synergy Index (ASI)** solver:
* **High Fasting Insulin:** The engine traverses paths to recommend *Ceylon Cinnamon + Magnesium + Acetic Acid* to structurally activate GLUT4 glucose transporters in muscle tissue.
* **Elevated Creatine Kinase (CK) / hs-CRP:** Flags severe tissue damage and systemic inflammation, shifting the user's active vector to a high-priority "Structural Repair" state and surfacing precise collagen-synthesis co-factors (Vitamin C + Copper + Proline).

Over time, sequential blood tests form a **Dynamic Biological Twin** inside ArcadeDB, allowing the machine learning layers to learn exactly how a specific human body dynamically reacts to micro-additive nutritional changes.

# References

https://www.biorxiv.org/content/10.1101/2024.10.12.618040v1

The point is this covers a lot more than just doet and exercises, and should enable anyone to personalise their own way to achieve their own biological goals. 
interactions with medicines, allergies, and more would be uniquely tracable for each user using medical research and open data to enable the broader society outside of research pursue the development of their own data. 

# tradeoffs

liability. there is none. you can only trust the outputs based on how effectively they have been, the quality of data provided, and whether ot actually works for you.
