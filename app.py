import streamlit as st

from utils import read_ply
from utils.ply_to_fig import plot_scatter3d


@st.cache_resource
def point_cloud_acquisition(uploaded_file = None):
    if uploaded_file is not None:
        Sidebar.success("File uploaded successfully!")
        
        points = read_ply.read_ply(uploaded_file)

        if points is not None:
            Sidebar.success("PLY file read successfully!")
            vertex_data = read_ply.get_vertex_data(points)
            if vertex_data is not None:
                x, y, z = read_ply.get_vertex_coordinates(vertex_data)
                Sidebar.success("Vertex data extracted successfully!")
                return x, y, z
            else:
                Sidebar.error("Failed to extract vertex data.")
        else:
            Sidebar.error("Failed to read PLY file.")
        
    else:
        Sidebar.warning("Please upload a PLY file to visualize.")
        return None, None, None


st.set_page_config(page_title="3D Viewer", layout="wide", initial_sidebar_state = "expanded")

Sidebar = st.sidebar

Sidebar.title("3D Point Cloud Viewer")

uploaded_file = Sidebar.file_uploader("Upload a PLY file", type=["ply"])

colorscales = [
    "Viridis", "Cividis", "Inferno", "Magma", "Plasma", "Turbo", "Jet",
    "Bluered", "RdBu", "Picnic", "Portland", "Blackbody", "Earth",
    "Electric", "Hot", "Rainbow", "YlGnBu", "Greens", "YlOrRd", "Agsunset"]


# Streamlit selectbox for choosing a colorscale
selected_colorscale = Sidebar.selectbox("Choose a colorscale:", colorscales)

PopOver =Sidebar.popover(label = "Subsample Point Cloud",help = "Subsample the point cloud data", use_container_width=True)

PopOver.write("Subsample Point Cloud to reduce resolution")
subsample_factor =PopOver.slider("Subsample Factor", min_value=1, max_value=100, value=1, step=1)


if Sidebar.button('Visualize'):
    x, y, z = point_cloud_acquisition(uploaded_file)
    x,y,z = read_ply.sample_data(x, y, z, subsample_factor)
    if selected_colorscale is None:
        selected_colorscale = 'viridis'
    
    if x is not None:

        fig = plot_scatter3d(x,y,z, selected_colorscale)

        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        
        else:
            st.error("Failed to create figure from PLY data.")
