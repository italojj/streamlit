import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

st.set_page_config(page_title="Network Analysis", layout="wide")
st.title("Analysis of the 'Artificial Intelligence in Education' Network")
st.write("This application displays the main structure of the related concepts network, and it can applied filters based in the user's preference to show the most relevant nodes.")

try:
    df = pd.read_csv("network_analysis.csv")
    

    st.sidebar.header("Analysis and Visualization Options")
    
    is_directed = st.sidebar.checkbox("Treat as a directed graph (with arrows)")
    
    if is_directed:
        G = nx.from_pandas_edgelist(df, 'source', 'target', create_using=nx.DiGraph())
    else:
        G = nx.from_pandas_edgelist(df, 'source', 'target')

    filter_type = st.sidebar.selectbox(
        "Display subgraph:",
        ("Full Network", 
         "High-Degree Subgraph")
    )

    G_to_display = G

    if filter_type == "High-Degree Subgraph":
        min_degree = st.sidebar.slider(
            "Keep nodes with a degree higher than:",
            min_value=0, max_value=max(dict(G.degree()).values()), value=5, step=1
        )
        selected_nodes = [n for n, d in G.degree() if d > min_degree]
        G_to_display = G.subgraph(selected_nodes)

    st.header(f"Statistical Analysis: {filter_type}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nodes (Vertices)", G_to_display.number_of_nodes())
    with col2:
        st.metric("Edges (Links)", G_to_display.number_of_edges())
    
    st.markdown("---")
    st.subheader("Structural Metrics")

    col1, col2, col3 = st.columns(3)
    with col1:
        density = nx.density(G_to_display)
        st.metric("Density / Sparsity", f"{density:.4f}")
        st.caption("Close to 1: dense network. Close to 0: sparse network.")
    
    with col2:
        try:
            assortativity = nx.degree_assortativity_coefficient(G_to_display)
            st.metric("Assortativity", f"{assortativity:.4f}")
            st.caption("> 0: Nodes connect to similar-degree nodes. < 0: Nodes connect to dissimilar-degree nodes.")
        except:
            st.metric("Assortativity", "N/A")
            st.caption("Not applicable for this network configuration.")

    with col3:
        clustering = nx.transitivity(G_to_display)
        st.metric("Global Clustering", f"{clustering:.4f}")
        st.caption("Measures the tendency of nodes to form 'triangles' or clusters.")

    st.markdown("---")
    st.subheader("Component Analysis")

    col1, col2 = st.columns(2)
    with col1:
        if is_directed:
            scc = nx.number_strongly_connected_components(G_to_display)
            st.metric("Strongly Connected Components", scc)
            st.caption("Groups where there is a path from A to B and B to A for every pair of nodes in the group.")
        else:
            st.info("The 'Strongly Connected Components' metric only applies to directed graphs.")

    with col2:
        if is_directed:
            wcc = nx.number_weakly_connected_components(G_to_display)
            st.metric("Weakly Connected Components", wcc)
            st.caption("Connected groups if we ignore the direction of the arrows.")
        else:
            cc = nx.number_connected_components(G_to_display)
            st.metric("Connected Components", cc)
            st.caption("Groups of nodes that are isolated from each other.")
    
    st.markdown("---")
    st.subheader("Degree Distribution")

    if G_to_display.number_of_nodes() > 0:
        if is_directed:
            degree_type = st.radio(
                "Select the degree type to display:",
                ('Total', 'In-degree', 'Out-degree')
            )
            if degree_type == 'Total':
                degrees = [d for n, d in G_to_display.degree()]
                title = "Total Degree Distribution"
            elif degree_type == 'In-degree':
                degrees = [d for n, d in G_to_display.in_degree()]
                title = "In-degree Distribution"
            else: # Out-degree
                degrees = [d for n, d in G_to_display.out_degree()]
                title = "Out-degree Distribution"
        else:
            degrees = [d for n, d in G_to_display.degree()]
            title = "Degree Distribution"

        fig, ax = plt.subplots()
        ax.hist(degrees, bins='auto', color='#007acc', alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel("Degree (Number of Connections)")
        ax.set_ylabel("Number of Nodes")
        st.pyplot(fig)
    else:
        st.info("No nodes to display in the histogram with the current filters.")

    st.markdown("---")
    st.subheader("Node Centrality Analysis")
    st.write("The table below shows the most important nodes in the network. Click on a column header to sort and see the ranking.")

    df_metrics = pd.DataFrame()
    if G_to_display.number_of_nodes() > 0:
        degree_c = nx.degree_centrality(G_to_display)
        betweenness_c = nx.betweenness_centrality(G_to_display)
        closeness_c = nx.closeness_centrality(G_to_display)
        try:
            eigenvector_c = nx.eigenvector_centrality(G_to_display, max_iter=500, tol=1e-05)
        except nx.PowerIterationFailedConvergence:
            eigenvector_c = {node: 0.0 for node in G_to_display.nodes()}
            st.warning("Eigenvector Centrality calculation did not converge.")

        df_metrics = pd.DataFrame({
            'Node': list(G_to_display.nodes()),
            'Degree': list(degree_c.values()),
            'Betweenness': list(betweenness_c.values()),
            'Closeness': list(closeness_c.values()),
            'Eigenvector': list(eigenvector_c.values())
        }).set_index('Node')

        st.dataframe(df_metrics.sort_values(by="Degree", ascending=False).style.format("{:.4f}"))

    st.sidebar.markdown("---")
    st.sidebar.header("Node Highlighting in Visualization")
    highlight_metric = st.sidebar.selectbox(
        "Highlight nodes by which metric?",
        ("None", "Degree", "Betweenness", "Closeness", "Eigenvector")
    )
    
    top_nodes = []
    if highlight_metric != "None" and not df_metrics.empty:
        top_k = st.sidebar.slider(
            "Number of nodes to highlight (Top-K):",
            min_value=1, max_value=20, value=5, step=1
        )
        top_nodes = df_metrics.sort_values(by=highlight_metric, ascending=False).head(top_k).index.tolist()

    st.sidebar.markdown("---")
    st.sidebar.header("Layout and Physics Options")
    layout_option = st.sidebar.selectbox(
        "Layout/Physics Algorithm:",
        ("Default (BarnesHut)", "Force Atlas 2", "Repulsion", "Physics Disabled")
    )

    st.header(f"Interactive Visualization: {filter_type}")
    net = Network(height='700px', width='100%', notebook=True, bgcolor="#222222", font_color="white", directed=is_directed)
    
    with st.spinner("Generating visualization..."):
        for node in G_to_display.nodes():
            color = "#97c2fc"
            size = 15
            if node in top_nodes:
                color = "#ff4b4b"
                size = 30
            net.add_node(node, label=node, color=color, size=size)
            
        for edge in G_to_display.edges():
            net.add_edge(edge[0], edge[1])

        if layout_option == "Force Atlas 2":
            net.force_atlas_2based()
        elif layout_option == "Repulsion":
            net.repulsion()
        elif layout_option == "Physics Disabled":
            net.toggle_physics(False)
        else:
            net.barnes_hut()

        net.show_buttons(filter_=True)
        html_content = net.generate_html()
        st.components.v1.html(html_content, height=720)

except FileNotFoundError:
    st.error("ERROR: The 'network_analysis.csv' file was not found in the repository. Please check the name.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
