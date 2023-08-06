import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="UzbekNLP",
    version="0.0.2",
    author="Maksud Sharipov, Ollabergan Yuldashov",
    author_email="maqsbek72@gmail.com",
    description="NLP library for Uzbek language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OllaberganYuldashov/UzbekNLP",
    project_urls={
        "Bug Tracker": "https://github.com/OllaberganYuldashov/UzbekNLP/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['python', 'UzbekNLP', 'uzbek words', 'NLP'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={"": ["*.xml"]},
    #package_data={"": ["cyr_exwords.csv", "lat_exwords.csv"],},
)