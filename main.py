import os

if __name__ == "__main__":
  port = 8501
  os.system(f"streamlit run app.py --server.port {port} --server.headless false")