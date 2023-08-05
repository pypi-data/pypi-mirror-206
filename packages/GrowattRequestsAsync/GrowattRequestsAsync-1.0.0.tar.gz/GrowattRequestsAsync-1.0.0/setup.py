import setuptools
import os

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="GrowattRequestsAsync",
    version="1.0.0",
    author="dwbruijn",
    description="Asynchronous API wrapper (client) for Growatt API which allows you to easily pull your data from Growatt servers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dwbruijn/GrowattRequestsAsync",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "httpx==0.24.0"
    ]
)