from setuptools import find_packages, setup

setup(
    name="AutoGenerateMKD",
    version="0.0.11",
    author="E-NoR,Teng",
    description="Auto generate markdown api docs, base on dosc.",
    packages=find_packages(),
    url="https://github.com/coseto6125/AutoGenerateMKD",
    project_urls={
        "Changelog": "https://github.com/coseto6125/AutoGenerateMKD/releases",
        "Download": "https://pypi.org/project/AutoGenerateMKD/#files",
        "PyPI": "https://pypi.org/project/AutoGenerateMKD/",
        "Source": "https://github.com/coseto6125/AutoGenerateMKD",
    },
    install_requires=[
        "mkdocs>=1",
        "wcmatch>=7",
        "mkdocs-awesome-pages-plugin>=2.5.0",
        "mkdocs>=1.4.3",
        "markdown-callouts>=0.3.0",
        "mkdocs-autorefs>=0.4.1",
        "mkdocs-awesome-pages-plugin>=2.9.0",
        "mkdocs-include-markdown-plugin>=4.0.4",
        "mkdocs-literate-nav>=0.6.0",
        "mkdocs-material>=1.1.1",
        "mkdocstrings-python>=0.9.0",
        "pymdown-extensions>=9.11",
        "mkdocs>=1",
        "wcmatch>=7",
        "mkdocs-awesome-pages-plugin>=2.5.0",
    ],
    include_package_data=True,
    data_files=[("", ["AutoGenerateMKD/mkdocs.yml"])],
    entry_points={
        "mkdocs.plugins": ["pagenav-generator = mkdocs_pagenav_generator.plugin:NavGeneratorPlugin"],
        "console_scripts": [
            "AutoGenMKD=AutoGenerateMKD.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
