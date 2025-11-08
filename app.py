import streamlit as st

st.set_page_config(page_title="Graph Theory App", layout="wide")

st.title("Graph Theory Multi-Menu App")

# Sidebar menu
page = st.sidebar.selectbox("Choose page:", ["Profil", "Graph Visualization", "Map Visualization"])

if page == "Profil":
    from pages import profil
elif page == "Graph Visualization":
    from pages import graph_visualization
elif page == "Map Visualization":
    from pages import map_visualization
