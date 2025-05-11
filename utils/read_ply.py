from plyfile import PlyData

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

def get_vertex_coordinates(vertex_data):
    """
    Extracts x, y, z coordinates from vertex data.

    :param vertex_data: Vertex data as a numpy structured array.
    :return: Tuple of x, y, z coordinates.
    """
    try:
        x = vertex_data['x']
        y = vertex_data['y']
        z = vertex_data['z']
        return x, y, z
    except Exception as e:
        print(f"Error extracting coordinates: {e}")
        return None, None, None

def sample_data(x, y, z, step):
    """
    Subsamples the x, y, z coordinates by a given step.

    :param x: X coordinates.
    :param y: Y coordinates.
    :param z: Z coordinates.
    :param step: Step size for subsampling.
    :return: Subsampled x, y, z coordinates.
    """
    try:
        return x[::step], y[::step], z[::step]
    except Exception as e:
        print(f"Error subsampling data: {e}")
        return None, None, None