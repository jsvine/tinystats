import sys
from setuptools import setup, find_packages

setup(
    name="tinystats",
    version="0.0.0",
    description="Command-line tool for fetching message, URL, and subscriber data for the TinyLetter newsletters you own.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="tinyletter",
    author="Jeremy Singer-Vine",
    author_email="jsvine@gmail.com",
    url="https://github.com/jsvine/tinystats",
    license="MIT",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "tinyapi",
        "unicodecsv"
    ],
    tests_require=[],
    entry_points={
        "console_scripts": [
            "tinystats = tinystats.cli:main",
        ]
    }
)
