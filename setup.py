from setuptools import setup, find_packages

setup(
    name="openphrasebank",
    version="0.1.1",
    author="Zhihao",
    author_email="liuzhihao109@foxmial.com",
    description="Customize phrasebanks from various texts or corpora.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/liuh886/open-phrasebank",
    install_requires=[
        'nltk', 
        'pymupdf',
        'tqdm',  
        'datasets', # Huggingface datasets
    ],
    extras_require={
        'spacy': ['spacy>=3.0', 'en_core_web_sm']
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'openphrasebank=openphrasebank.cli:main',  # Adjust according to your package structure
        ],
    },
    package_dir={"": "openphrasebank"},
    packages=find_packages(where="openphrasebank"),
    include_package_data=True,  # This tells setuptools to check MANIFEST.in
    package_data={
        "": ["data/*", "phrasebanks/*"],  # include all files in the data and phrasebanks directories
    },
)