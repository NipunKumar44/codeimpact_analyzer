# 🔍 Code Impact Analyzer

<p align="center">
  <img src="assets/codeimpact.gif" alt="Code Impact Analyzer Demo" width="850"/>
</p>

**Code Impact Analyzer** is an AI-powered static code analysis tool designed to detect downstream dependency impacts across backend services. By mapping function relationships and using Local LLMs, it helps developers understand the "blast radius" of code changes before they are committed.

Built using **Python AST parsing**, **NetworkX dependency graphs**, **Streamlit**, and **Ollama**.

---

## 🛠 Tech Stack

* **Language:** Python 3.9+
* **UI Framework:** Streamlit
* **Graph Logic:** NetworkX & Matplotlib
* **LLM Engine:** Ollama (Local AI)
* **Analysis Engine:** AST (Abstract Syntax Tree)

---

## 📂 Project Structure

```text
CodeImpactAnalyzer/
│
├── app.py              # Main Streamlit application
├── parser.py           # AST logic for extracting functions and calls
├── graph_builder.py    # Logic for building and styling the NetworkX graph
├── analyzer.py         # Risk scoring and Ollama API integration
│
├── sample_project/     # Example directory for testing the tool
│   └── payments.py
│
├── assets/             # Documentation images and gifs
│   └── codeimpact.gif
│
└── README.md           # Project documentation
