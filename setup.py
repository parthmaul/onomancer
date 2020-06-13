import setuptools
from pathlib import Path

NAME = 'onomancer'

with open("README.md", "r") as fh:
    long_description = fh.read()


# What packages are required for this module to be executed?
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setuptools.setup(
    name="onomancer",
    version=about['__version__'],
    author="Parth Jalundhwala",
    author_email="pjalundh@gmail.com",
    description="Lookup and/or predict gender of given first name.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parthmaul/onomancer",
    packages=setuptools.find_packages(),
    install_requires=list_reqs(),
    package_data={'onomancer': ['data/*.txt', 'data/*.bin']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=["gender", "predict","names","model","nlp"],
)
