import streamlit as st

from utils.read_ply import read_ply
from utils.ply_to_fig import ply_to_fig

st.set_page_config(page_title="3D Viewer", layout="wide")

st.sidebar.title("3D Viewer - PLY File Reader")

uploaded_file = st.sidebar.file_uploader("Upload a PLY file", type=["ply"])

if uploaded_file is not None:
    st.sidebar.success("File uploaded successfully!")
    points = read_ply(uploaded_file)

    if points is not None:
        fig = ply_to_fig(points)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to create figure from PLY data.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    