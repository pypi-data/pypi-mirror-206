from setuptools import setup, find_packages
from pathlib import Path

# read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="cmo_dataexplore",
    version="0.0.1",
    python_requires='>=3.6',
    description='Basic data exploration, fast and easy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jeanine Schoonemann',
    author_email='service@cmotions.nl',
    url='https://dev.azure.com/Cmotions/Packages/_git/cmo_dataexplore',
    packages=find_packages(),
    install_requires=[
        "scikit-learn>=0.20.2",
        "ppscore>=1.2.0",
        "cmo-dataviz",
    ],
    extras_require={
        'dev': [
            'black', 
            'jupyterlab', 
            'pytest>=6.2.4',
            'ipykernel',
            'twine',
        ],
    },
    # files to be shipped with the installation
    # after installation, these can be found with the functions in resources.py
    package_data={
        "cmo_dataexplore": [
            "data/*.csv",
            "notebooks/*tutorial*.ipynb",
        ]
    },
)