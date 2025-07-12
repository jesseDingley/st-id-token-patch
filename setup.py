# setup.py
from setuptools import setup
from setuptools.command.install import install
import os

class PostInstallCommand(install):
    """Post-installation to patch streamlit."""
    def run(self):
        import patch  # this must import and run the patch function
        print("hello")
        super().run()

setup(
    name="streamlit_id_token_patch",
    version="0.1",
    data_files=[("site-packages", ["patch.pth"])],
    py_modules=["patch"],  # assuming patch.py is in the root
    cmdclass={
        'install': PostInstallCommand,
    },
)