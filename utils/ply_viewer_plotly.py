import numpy as np
import plotly.graph_objects as go
from plyfile import PlyData  # You might need to install this: pip install plyfile


def view_ply_colored_by_height(file_path):
    try:
        plydata = PlyData.read(file_path)

        if 'vertex' in plydata:
            vertex = plydata['vertex'].data
            x = vertex['x']
            y = vertex['y']
            z = vertex['z']

            # Determine color based on height (z-coordinate)
            colors = z  # You can normalize or scale these values if needed
            colormap = 'viridis'  # Choose a Plotly colormap (e.g., 'viridis', 'plasma', 'magma')

            fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                               mode='markers',
                                               marker=dict(size=2,
                                                           color=colors,
                                                           colorscale=colormap,
                                                           colorbar=dict(title='Height (Z-axis)')))])
            fig.update_layout(scene=dict(zaxis_title='Height'))
            fig.show()

        elif 'face' in plydata:
            faces = plydata['face'].data['vertex_indices']
            vertices = plydata['vertex'].data
            x = vertices['x']
            y = vertices['y']
            z = vertices['z']

            i = np.array([face[0] for face in faces])
            j = np.array([face[1] for face in faces])
            k = np.array([face[2] for face in faces])

            # Determine color based on vertex height (z-coordinate)
            vertex_colors = z
            colormap = 'viridis'

            fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k,
                                         vertexcolor=[[c] * 3 for c in vertex_colors],  # Assign color per vertex
                                         colorscale=colormap,
                                         colorbar=dict(title='Height (Z-axis)'),
                                         opacity=0.8)])
            fig.update_layout(scene=dict(zaxis_title='Height'))
            fig.show()

        else:
            print(f"PLY file {file_path} does not contain 'vertex' or 'face' data.")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  ply_file = "/home/hirur/SupportTool/3DViewer/cloud_20250429_013942.ply"
  view_ply_colored_by_height(ply_file)