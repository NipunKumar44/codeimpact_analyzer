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

```text
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
└── README.md
