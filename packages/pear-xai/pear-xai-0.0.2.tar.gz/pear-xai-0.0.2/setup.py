import os
import sys
from io import open

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(here, "pear"))

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Manually install torch since the torchsort setup script requires this
# the torch package is also listed in install_requires as this seems to be needed too
os.system("pip install torch==1.11.0")

setup(name="pear-xai",
      version="v0.0.2",
      description="PEAR: Post-hoc Explainer Agreement Regularization",
      url="https://arthur.ai",
      keywords=["pytorch", "XAI", "machine learning"],
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      include_package_data=True,
      package_data={"": ["datasets/*/*.csv"]},
      python_requires=">=3.9",
      install_requires=[
          "jupyter==1.0.0",
          "lime==0.2.0.1",
          "matplotlib==3.5.2",
          "numpy==1.23.2",
          "scikit-learn==1.2.2",
          "seaborn==0.12.2",
          "shap==0.41.0",
          "sklearn==0.0",
          "tabulate==0.8.10",
          "torch==1.11.0",
          "torchvision==0.12.0",
          "tqdm==4.64.0",
          "torchsort==0.1.9"],
      license="BSD3")

