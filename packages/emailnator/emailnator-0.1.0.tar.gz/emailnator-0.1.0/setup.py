from setuptools import setup, find_packages
from os import path

# Read the contents of README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="emailnator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    author="repollo",
    author_email="repollo.marrero@gmail.com",
    description="A Python wrapper for the Emailnator temporary email service.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Add this line
    keywords="emailnator wrapper temporary email",
    url="https://github.com/repollo/emailnator",
)
