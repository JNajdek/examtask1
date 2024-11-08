"""
Package setup information
"""
from setuptools import setup, find_packages

setup(
    name="circles",
    version="1.0",
    author="Jakub Najdek",
    packages=find_packages('src', exclude=['test']),
    package_dir={"": "src"},
)
