from setuptools import setup, find_packages

with open("README.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="MSO_WT",
    version="0.0.1",
    author="Apostolos Evangelidis",
    author_email="apostolosev@gmail.com",
    description="Official python implementation of the Maximal Spectral Overlap Wavelet Transform (MSO-WT)",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/apostolosev/MSO_WT",
    project_urls = {
        "Bug Tracker": "https://github.com/apostolosev/MSO_WT/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["numpy", "scipy", "pywavelets"],
    python_requires = ">=3.6"
)
