from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="snirhcrawler",
    version="0.1.0",
    author="Francisco B Macedo",
    author_email="your-email@example.com",
    description="A brief description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/franciscobmacedo/snirhcrawler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "beautifulsoup4~=4.10.0",
        "pydantic~=1.9.0",
        "requests~=2.27.1",
        "pandas~=1.4.1",
        "lxml~=5.2.1",
    ],
)
