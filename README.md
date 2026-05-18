
# ArguFormer
## v2 in progress

ArgueFromer is a **NLP system for analyzing debate transcripts** using both **traditional machine learning** and **modern transformer models**, enabling comparative analysis of argumentative language.

The system detects:

* Speaker segmentation
* Sentiment of arguments
* Toxic language
* Logical fallacies
* Model comparison between classical NLP and transformer models

It demonstrates the evolution of NLP approaches from **feature-engineered models** to **transformer-based language models**.

---

# Table of Contents

* [Overview](#overview)
* [System Architecture](#system-architecture)
* [Installation](#installation)
* [Project Structure](#project-structure)

---

# Overview

Debates often contain complex argumentative structures including **emotional appeals, logical fallacies, and toxic rhetoric**. Automatically analyzing such patterns can help in studying argument quality and discourse dynamics.

The **Arguformer** processes debate transcripts and performs multi-stage analysis:

1. **Speaker Segmentation**
   Extracts individual statements from debate transcripts.

2. **Sentiment Analysis**
   Detects whether arguments express positive or negative sentiment.

3. **Toxicity Detection**
   Identifies abusive or harmful language.

4. **Fallacy Detection**

   * **Version 1 (Traditional NLP)**
     Uses **TF-IDF + Logistic Regression**.
   * **Version 2 (Transformer NLP)**
     Uses **DistilBERT fallacy classification**.

5. **Model Comparison**
   Both models are executed in parallel and their predictions are compared to produce a **final judgement**.

This approach highlights the strengths and limitations of both **classical NLP pipelines and transformer models**.

---

# System Architecture

```
Debate Transcript
        │
        ▼
Speaker Segmentation
        │
        ▼
Sentence Level Analysis
        │
 ┌───────────────┬─────────────────┐
 │               │                 │
 ▼               ▼                 ▼
Traditional NLP  Sentiment Model   Toxicity Model
TF-IDF + LR      (DistilBERT)       (Toxic-BERT)
 │
 ▼
Fallacy Prediction
 │
 ▼
Transformer Fallacy Model
(DistilBERT)
 │
 ▼
Model Comparison Engine
 │
 ▼
Final Debate Analysis Output
```

The architecture enables **parallel analysis pipelines**, allowing comparison between **feature-engineered ML methods** and **deep transformer models**.

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Atim45/ArguFormer.git
cd ArguFormer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Project

```bash
python main.py
```
Example input debate:

```
Speaker A: You are the dumbest person alive
Speaker B: That argument makes no sense
Speaker A: Think about the poor children suffering
```

Example output:

```
Speaker   Sentence                         Sentiment   Toxicity   Final Judgement
----------------------------------------------------------------------------------
Speaker A You are the dumbest person alive NEGATIVE    toxic      Ad Hominem
Speaker B That argument makes no sense     NEGATIVE    toxic      Strawman
Speaker A Think about the poor children    POSITIVE    non-toxic  Appeal to Emotion
```

---

# Project Structure

```
arguformer/

├── cli/
│   ├── __init__.py
│   └── args.py

├── core/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── segmentation.py
│   └── comparison_engine.py

├── models/
│   ├── __init__.py
│   ├── fallacy_lr.py
│   ├── fallacy_transformer.py
│   └── manager.py   ← soon

├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── exceptions.py
│   └── config_loader.py

├── configs/
│   └── default.yaml

├── datasets/
├── evaluation/
├── logs/
├── outputs/
├── tests/
├── rag/

├── main.py
├── requirements.txt
├── README.md
└── .gitignore
---

# Technologies Used

* Python
* HuggingFace Transformers
* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* DistilBERT
* Toxic-BERT

---

# Future Improvements

Potential future upgrades include:

* Larger **debate datasets**
* Improved **fallacy classification models**
* **Visualization dashboards**
* **Argument strength scoring**
* **persuasion technique detection**


