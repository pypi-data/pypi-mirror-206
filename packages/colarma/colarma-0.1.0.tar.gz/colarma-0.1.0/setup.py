from setuptools import setup, find_packages

setup(
    name="colarma",
    version="0.1.0",
    author="Votre nom",
    author_email="votre.email@example.com",
    description="Colarma est un module Python simple et facile à utiliser pour travailler avec les couleurs. Il fournit des fonctionnalités pour convertir les formats de couleur, manipuler les couleurs et créer des palettes de couleurs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anyiskiidd/colarma",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
