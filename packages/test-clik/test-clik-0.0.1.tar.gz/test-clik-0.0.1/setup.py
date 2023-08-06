from setuptools import setup, find_packages

with open("./README.md", "r", encoding="utf-8") as e:
    long_description = e.read()

setup(
    name="test-clik",
    version="0.0.1",
    author="Dxsxsx",
    author_email="123@pm.me",
    description="test clip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dxsxsx",
    package_dir={"":"src"},
    packages=find_packages(where='src'),
    install_requires=["flet", "click==8.1.3", "click"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["test-init=test_clik.cli:init"],
    },
    keywords=["python web template", "web application", "development"],
)