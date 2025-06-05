import streamlit as st
import plotly.graph_objects as go
import numpy as np


def plot_scatter3d(x=None, y=None,z=None, selected_colorscale = 'viridis'):
     
    try:
        if x is None or y is None or z is None:
            raise ValueError("X, Y, and Z coordinates must be provided.")
            return None
        else:
                

            # Color by Z-coordinate (height) if no explicit colors
            marker_config = dict(size=2, color=z, colorscale= selected_colorscale, colorbar=dict(title='Z'))

            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                                mode='markers',
                                                marker=marker_config)])

            fig.update_layout(
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z',
                    aspectmode='data',
                    xaxis=dict(
                        visible=True, # Ensure X-axis is visible
                        showbackground=True,
                        backgroundcolor="rgba(0, 0, 0, 0.05)", # Light background for the grid
                        gridcolor="lightgrey", # Color of grid lines
                        linecolor="black", # Color of the axis line
                        zerolinecolor="black" # Color of the zero line
                    ),
                    yaxis=dict(
                        visible=True, # Ensure Y-axis is visible
                        showbackground=True,
                        backgroundcolor="rgba(0, 0, 0, 0.05)",
                        gridcolor="lightgrey",
                        linecolor="black",
                        zerolinecolor="black"
                    ),
                    zaxis=dict(
                        visible=True, # Ensure Z-axis is visible
                        showbackground=True,
                        backgroundcolor="rgba(0, 0, 0, 0.05)",
                        gridcolor="lightgrey",
                        linecolor="black",
                        zerolinecolor="black"
                    )
                
                ),
                autosize=False,
                width=1200,  # Adjust overall width
                height=800,   # Adjust overall height
                margin=dict(l=40, r=40, b=40, t=40)  # Adjust margins
            )
            return fig
    
    except Exception as e:
        st.error(f"Error creating point cloud figure: {e}")
        return None


def ply_to_fig(ply_data, selected_colorscale = 'viridis'):
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

            # Color by Z-coordinate (height) if no explicit colors
            marker_config = dict(size=2, color=z, colorscale= selected_colorscale, colorbar=dict(title='Z'))

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
