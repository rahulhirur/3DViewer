import streamlit as st

from utils.read_ply import read_ply
from utils.ply_to_fig import ply_to_fig

st.set_page_config(page_title="3D Viewer", layout="wide", initial_sidebar_state = "expanded")

st.sidebar.title("3D Point Cloud Viewer")

uploaded_file = st.sidebar.file_uploader("Upload a PLY file", type=["ply"])

colorscales = [
    "Viridis", "Cividis", "Inferno", "Magma", "Plasma", "Turbo", "Jet",
    "Bluered", "RdBu", "Picnic", "Portland", "Blackbody", "Earth",
    "Electric", "Hot", "Rainbow", "YlGnBu", "Greens", "YlOrRd", "Agsunset"]


# Streamlit selectbox for choosing a colorscale
selected_colorscale = st.sidebar.selectbox("Choose a colorscale:", colorscales)


if uploaded_file is not None:
    st.sidebar.success("File uploaded successfully!")
    points = read_ply(uploaded_file)

if st.sidebar.button('Visualize'):
    
    if selected_colorscale is None:
        selected_colorscale = 'viridis'
    
    if points is not None:
        fig = ply_to_fig(points, selected_colorscale)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to create figure from PLY data.")
