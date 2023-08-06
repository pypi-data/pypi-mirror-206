import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_spinner", 
    version="0.1.0",
    author="wooy0ng",
    author_email="yygg9800@naver.com",
    description="Simple Spinner in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wooy0ng/simple_spinner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)