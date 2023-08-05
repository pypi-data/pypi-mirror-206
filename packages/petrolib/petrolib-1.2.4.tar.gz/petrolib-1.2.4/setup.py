import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "petrolib",
    version = "1.2.4",
    author = "Joshua Atolagbe",
    author_email = "atolagbejoshua2@gmail.com",
    description = "A Python package for petrophysics and formation evaluation",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/joshua-atolagbe/petrolib",
    project_urls = {
        "Bug Tracker": "https://github.com/joshua-atolagbe/petrolib/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    packages = setuptools.find_packages(),
    python_requires = ">=3.5",
    install_requires=[
        'matplotlib', 'pandas', 'numpy', 'geopandas', 'contextily', 'scipy', 'seaborn'
        ]
)