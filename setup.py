# setup.py
from setuptools import setup

setup(
    name="streamlit_id_token_patch",
    version="0.1",
    py_modules=["patch"],
    data_files=[("site-packages", ["patch.pth"])],
    description="Monkey patch for Streamlit to expose ID token",
)
