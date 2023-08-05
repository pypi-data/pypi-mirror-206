from setuptools import setup, find_packages
with open("README.md") as desc:
    ldsc = desc.read()

setup(
    name="catnapmodule",
    version="1.3",
    packages=find_packages(),
    author="Nap the Cat",
    author_email="mohulhack@gmail.com",
    long_description=ldsc
)
