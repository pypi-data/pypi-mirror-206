from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()
setup(
    name="test-clik",
    version="0.0.3",
    author="Dxsxsx",
    author_email="psdd@pm.me",
    description="Web Boilerplate for Flet Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dxsxsx",
    packages=["logic"],
    install_requires=["click", "flet"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["fletxible-init=logic.cli:init"],
    },
    keywords=["python web template", "web application", "development"],
)