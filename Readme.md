# Code Impact Analyzer

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

```text id="a1m9k2"
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
└── README.md
```

---

# How It Works

## 1. Parse Source Code

The system parses Python source files using the AST module and extracts:

* Functions
* Function calls
* Dependencies

---

## 2. Build Dependency Graph

Using NetworkX, the tool creates a directed graph representing relationships between functions.

Example:

```text id="r7k2p5"
validate_user → process_payment → checkout
```

---

## 3. Analyze Impact

When a function is selected, the analyzer identifies:

* Dependent functions
* Downstream impact
* Potentially affected modules

---

## 4. Generate Impact Report

The system generates:

* AI Summary
* Risk Level
* Recommended Testing Strategy

---

# Installation

## Clone Repository

```bash id="m8v1q4"
git clone <your-repository-url>
cd CodeImpactAnalyzer
```

---

## Install Dependencies

```bash id="p3x7k1"
pip install streamlit networkx matplotlib ollama
```

---

## Install Ollama

Download and install Ollama:

[Ollama Official Website](https://ollama.com?utm_source=chatgpt.com)

---

## Pull Model

```bash id="y4m8r2"
ollama pull deepseek-coder
```

---

# Run Application

```bash id="q2k9p6"
streamlit run app.py
```

---

# Sample Queries

Try entering:

```text id="t6v3m1"
validate_user
process_payment
generate_invoice
send_email
```

---

# Example Output

## Impact Summary

```text id="b5r8x2"
Changing send_email impacts checkout with LOW risk.
```

## Risk Level

```text id="v1k7m4"
LOW
```

## Recommended Testing

```text id="u8p2q5"
- Run regression tests
- Verify dependency workflows
- Validate integration paths
```

---

# Risk Classification Logic

| Affected Functions Count | Risk Level |
| ------------------------ | ---------- |
| 1                        | LOW        |
| 2                        | MEDIUM     |
| 3+                       | HIGH       |

---

# Future Improvements

* Multi-file project parsing
* ZIP project upload support
* Class-level dependency analysis
* API endpoint impact analysis
* LangGraph multi-agent workflows
* Git integration
* CI/CD integration
* Advanced LLM-based recommendations

---

# Use Cases

* Change impact analysis
* Dependency tracking
* Regression risk detection
* Backend architecture visualization
* Developer productivity tooling

---

# Author

Developed as a prototype AI-assisted developer tool for static dependency and impact analysis.
