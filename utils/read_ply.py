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