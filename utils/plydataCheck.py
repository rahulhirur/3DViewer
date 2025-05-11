from plyfile import PlyData
import numpy as np
import plotly.graph_objects as go

def read_ply(file_path):
    """
    Reads a PLY file and returns its data.

    :param file_path: Path to the PLY file.
    :return: PlyData object containing the PLY file data.
    """
    try:
        ply_data = PlyData.read(file_path)
        return ply_data
    except Exception as e:
        print(f"Error reading PLY file: {e}")
        return None
    
def get_vertex_data(ply_data):
    """
    Extracts vertex data from a PlyData object.

    :param ply_data: PlyData object containing the PLY file data.
    :return: Vertex data as a numpy structured array.
    """
    try:
        if 'vertex' in ply_data:
            return ply_data['vertex'].data
        else:
            print("No vertex data found in PLY file.")
            return None
    except Exception as e:
        print(f"Error extracting vertex data: {e}")
        return None


file_path = '/home/hirur/SupportTool/3DViewer/cloud_20250429_013942.ply'

ply_data = read_ply(file_path)

vertex_data = get_vertex_data(ply_data)

if vertex_data is not None:
    print("Vertex data extracted successfully.")
    
    x = vertex_data['x']
    y = vertex_data['y']
    z = vertex_data['z']

    # subsample the x array for every nth point and n is defined step
    step = 1
    print(len(x))
    print(len(x[::step]))

    fig = go.Figure(data=[go.Scatter3d(x=x[::step], y=y[::step], z=z[::step],
                                            mode='markers',
                                            marker=dict(size=2,
                                                        color=z[::step],  # Color by Z-coordinate
                                                        colorscale="viridis",
                                                        colorbar=dict(title='Height (Z-axis)')))])
    fig.show()
    
