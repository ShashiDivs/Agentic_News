from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="News-Agent",
    version="0.1",
    author="Shashi",
    packages=find_packages(),
    install_requires = requirements,
)