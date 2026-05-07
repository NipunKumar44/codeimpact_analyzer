import streamlit as st
import ollama
import matplotlib.pyplot as plt
import networkx as nx

from parser import parse_file
from graph_builder import build_graph
from analyzer import find_impacted

# ---------------- TITLE ----------------

st.title("AI-Powered Code Impact Analyzer")

st.write(
    "Static analysis tool for detecting downstream dependency impact across backend services."
)

st.caption(
    "Built using Python AST parsing, NetworkX dependency graphs, Streamlit, and Ollama."
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("Sample Queries")

st.sidebar.write("validate_user")
st.sidebar.write("process_payment")
st.sidebar.write("generate_invoice")
st.sidebar.write("send_email")

# ---------------- INPUT ----------------

target = st.text_input("Enter function name")

# ---------------- SESSION STATE ----------------

if "result" not in st.session_state:
    st.session_state.result = None

if "risk" not in st.session_state:
    st.session_state.risk = None

if "graph" not in st.session_state:
    st.session_state.graph = None

# ---------------- ANALYZE BUTTON ----------------

if st.button("Analyze"):

    # Parse project
    parsed = parse_file("sample_project/payments.py")

    # Build dependency graph
    graph = build_graph(parsed)

    # Save graph
    st.session_state.graph = graph

    # Find impacted functions
    result = find_impacted(graph, target)

    st.session_state.result = result

    # ---------------- RISK CALCULATION ----------------

    risk = "LOW"

    if len(result) >= 3:
        risk = "HIGH"

    elif len(result) >= 2:
        risk = "MEDIUM"

    st.session_state.risk = risk

# ---------------- SHOW RESULTS ----------------

if st.session_state.result is not None:

    graph = st.session_state.graph
    result = st.session_state.result
    risk = st.session_state.risk

    # ---------------- GRAPH ----------------

    st.subheader("Dependency Graph")

    fig, ax = plt.subplots(figsize=(14, 10))

    pos = nx.spring_layout(
        graph,
        k=3,
        iterations=200,
        seed=42
    )

    # ---------------- NODE COLORS ----------------

    node_colors = []

    for node in graph.nodes():

        # Selected function
        if node == target:
            node_colors.append("red")

        # Impacted functions
        elif node in result:
            node_colors.append("orange")

        # Other functions
        else:
            node_colors.append("skyblue")

    # ---------------- DRAW GRAPH ----------------

    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=4000,
        node_color=node_colors,
        ax=ax
    )

    nx.draw_networkx_edges(
        graph,
        pos,
        arrows=True,
        arrowsize=20,
        ax=ax
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=9,
        font_weight="bold",
        ax=ax
    )

    plt.axis("off")

    st.pyplot(fig)

    # ---------------- IMPACTED FUNCTIONS ----------------

    st.subheader("Affected Functions")

    if result:
        for r in result:
            st.write("-", r)
    else:
        st.write("No affected functions")

    # ---------------- METRIC ----------------

    st.metric("Affected Functions Count", len(result))

    # ---------------- RISK LEVEL ----------------

    st.subheader("Risk Level")

    if risk == "HIGH":
        st.error(risk)

    elif risk == "MEDIUM":
        st.warning(risk)

    else:
        st.success(risk)

    # ---------------- AI REPORT BUTTON ----------------

    if st.button("Generate AI Report"):

        # ---------------- AI PROMPT ----------------

        prompt = f"""
Reply with ONLY ONE short line.

Format:
Changing <function> impacts <affected functions> with <risk> risk.

Use the provided values only.

Function: {target}
Affected: {result}
Risk: {risk}
"""

        try:

            response = ollama.chat(
                model='deepseek-coder',
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )

            ai_summary = response['message']['content']

        except:

            ai_summary = "AI summary unavailable."

        # ---------------- FINAL REPORT ----------------

        st.subheader("Impact Analysis Report")

        st.markdown(f"""
### AI Summary
- {ai_summary}

### Risk Level
- {risk}

### Recommended Testing
- Run regression tests
- Verify dependency workflows
- Validate integration paths
""")

        st.success("Impact analysis completed successfully.")