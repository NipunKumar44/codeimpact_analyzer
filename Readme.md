# Code Impact Analyzer

<p align="center">
  <img src="assets/codeimpact.gif" alt="Code Impact Analyzer Demo" width="850"/>
</p>

AI-powered static code analysis tool for detecting downstream dependency impact across backend services.

Built using Python AST parsing, NetworkX dependency graphs, Streamlit, and Ollama.

---

# Features

* Static source code parsing using Python AST
* Function dependency tracking
* Downstream impact analysis
* Interactive dependency graph visualization
* Risk level classification (Low / Medium / High)
* AI-generated impact summaries using Ollama
* Streamlit-based interactive UI
* Highlighted impacted functions in dependency graph

---

# Tech Stack

* Python
* Streamlit
* NetworkX
* Matplotlib
* Ollama
* AST (Abstract Syntax Tree)

---

# Project Structure

CodeImpactAnalyzer/
│
├── app.py
├── parser.py
├── graph_builder.py
├── analyzer.py
│
├── sample_project/
│   └── payments.py
│
├── assets/
│   └── codeimpact.gif
│
├── requirements.txt
└── README.md

---

# How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/your-username/CodeImpactAnalyzer.git
cd CodeImpactAnalyzer
2. Create virtual environment
ollama run llama3
5. Run app
streamlit run app.py
6. Open in browser

http://localhost:8501

Output Preview
Parse Python files
Build dependency graphs
Highlight impacted functions
Generate AI impact summaries
Interactive visualization
