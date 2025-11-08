# app.py
import os
os.environ["STREAMLIT_WATCHDOG_DISABLE"] = "true"

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Simple Graph App")

# Buat graph sederhana
G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,4),(3,4),(4,5)])

# Visualisasi dengan matplotlib
fig, ax = plt.subplots()
nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray", node_size=1000, ax=ax)
st.pyplot(fig)
