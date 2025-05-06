import streamlit as st
import plotly.graph_objects as go
import numpy as np





def ply_to_fig(ply_data):
    """
    Creates a Plotly Figure object for a 3D point cloud from PLY data.

    Args:
        ply_data (PlyData): A PlyData object containing vertex information.

    Returns:
        plotly.graph_objects.Figure: A Plotly Figure object displaying the 3D point cloud.
    """
    try:
        if 'vertex' in ply_data:
            vertex = ply_data['vertex'].data
            x = vertex['x']
            y = vertex['y']
            z = vertex['z']

            # You might have color information in the PLY file as well
            if 'red' in vertex.dtype.names and 'green' in vertex.dtype.names and 'blue' in vertex.dtype.names:
                colors = np.vstack((vertex['red'], vertex['green'], vertex['blue'])).T / 255.0
                marker_config = dict(size=2, color=colors)
            else:
                # Color by Z-coordinate (height) if no explicit colors
                marker_config = dict(size=2, color=z, colorscale='viridis', colorbar=dict(title='Z'))

            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                               mode='markers',
                                               marker=marker_config)])

            fig.update_layout(
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    aspectmode='data'  # Adjust as needed
                ),
                autosize=False,
                width=1200,  # Adjust overall width
                height=800,   # Adjust overall height
                margin=dict(l=40, r=40, b=40, t=40)  # Adjust margins
            )
            return fig
        
        else:
            st.error("PLY file does not contain vertex information.")
            return None
    
    except Exception as e:
        st.error(f"Error creating point cloud figure: {e}")
        return None