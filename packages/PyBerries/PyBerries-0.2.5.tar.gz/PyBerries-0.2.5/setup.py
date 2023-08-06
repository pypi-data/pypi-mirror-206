import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBerries",
    version="0.2.5",
    author="Daniel Thedie",
    author_email="daniel.thedie@ed.ac.uk",
    description="Processing of Bacmman measurement tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/MEKlab/pyberries",
    packages=setuptools.find_packages(where='pyberries'),
    package_dir={"": "pyberries"},
    python_requires='>=3.8',
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib', 'tifffile', 'h5py','seaborn', 'pybacmman', 'IPython']
)
