# Code Impact Analyzer

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph-FF6B6B?style=for-the-badge&logo=networkx)](https://networkx.org/)
[![Ollama](https://img.shields.io/badge/Ollama-LocalAI-4A90E2?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

<p align="center">
  <img src="assets/codeimpact.gif" alt="Code Impact Analyzer Demo" width="850"/>
</p>

**Code Impact Analyzer** is an AI-powered static code analysis tool designed to detect downstream dependency impacts across backend services. By mapping function relationships and using Local LLMs, it helps developers understand the "blast radius" of code changes before they are committed.

Built with **Python AST parsing**, **NetworkX dependency graphs**, **Streamlit**, and **Ollama**.

---

## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| ![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white) | Core language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Web UI framework |
| ![NetworkX](https://img.shields.io/badge/NetworkX-Graph_Analysis-FF6B6B?style=flat-square&logo=python) | Graph analysis |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-0071C5?style=flat-square&logo=matplotlib) | Visualization |
| ![Ollama](https://img.shields.io/badge/Ollama-Local_AI-4A90E2?style=flat-square&logo=ollama) | Local LLM |
| ![AST](https://img.shields.io/badge/AST-Parsing-3776AB?style=flat-square&logo=python) | Code analysis |

---

## 📂 Project Structure

```
CodeImpact Analyzer/
│
├── 🎯 app.py                  Main Streamlit application entry point
├── 🔍 parser.py               AST logic for extracting functions and calls
├── 📈 graph_builder.py        NetworkX dependency graph building & styling
├── 🤖 analyzer.py             Risk scoring & Ollama LLM integration
│
├── 📦 sample_project/         Example project for testing & demonstration
│   └── payments.py
│
├── 🎬 assets/                 Documentation media (images, GIFs, etc.)
│   └── codeimpact.gif
│
└── 📖 README.md               Project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CodeImpactAnalyzer.git
cd CodeImpactAnalyzer
```

### 2. Set Up a Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Initialize AI Model (Ollama)

Ensure you have Ollama installed and running on your machine.

```bash
ollama pull llama3
ollama run llama3
```

### 4. Run the Application

```bash
streamlit run app.py
```

### 5. Access the Dashboard

Open your browser and navigate to:

```
http://localhost:8501
```

---

## 📖 Features

- ✨ **AST-based Code Analysis** — Automatically extracts functions and dependencies from Python code
- 📊 **Dependency Graph Visualization** — Visual representation of code dependencies using NetworkX
- ⚡ **Risk Scoring** — AI-powered impact assessment using Ollama
- 🎨 **Interactive Dashboard** — User-friendly Streamlit interface
- 🔒 **Local LLM Integration** — Privacy-first analysis with local AI models

---

## 💡 How It Works

1. **Parse:** Extract functions and calls from Python files using AST
2. **Analyze:** Build a dependency graph to understand relationships
3. **Score:** Use local LLM to assess the impact of code changes
4. **Visualize:** Display interactive graphs on the Streamlit dashboard

---

<div align="center">
  <p>Made with ❤️ for developers who care about code quality</p>
</div>
