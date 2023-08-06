from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gotji",
    version="1.0.3",
    description="Dev by Meoaw",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/exaDev99/gotji",
    author="exaDev99",
    author_email="meoawdev.me@gmail.com",
    license="MIT",
    packages=["gotji"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "pystyle"
    ],
)
