from setuptools import setup
from setuptools import find_packages



with open("README.md") as f:
    long_description = f.read()

setup(
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["*.json", "*.yaml", "*.ini"]},
    include_package_data=True,
    entry_points={"console_scripts": ["nexora=nexora.cli.autotuna:main"]},
    long_description=long_description,
)
