import streamlit as st
import graph_visualization
import map_visualization
import profil

# ===========================
# Nonaktifkan watcher untuk deploy Streamlit Cloud
# ===========================
st.set_option('server.fileWatcherType', 'none')

# ===========================
# Sidebar menu
# ===========================
page = st.sidebar.selectbox(
    "Choose page:",
    ["Profil", "Graph Visualization", "Map Visualization"]
)

# ===========================
# Halaman utama sesuai pilihan
# ===========================
if page == "Profil":
    profil.main()
elif page == "Graph Visualization":
    graph_visualization.main()
elif page == "Map Visualization":
    map_visualization.main()
