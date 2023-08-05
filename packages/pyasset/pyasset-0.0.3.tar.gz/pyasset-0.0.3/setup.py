import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyasset", # Replace with your own username
    version="0.0.3",
    author="kimssammwu",
    author_email="dlalsdn1009@naver.com",
    description="many pattern in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dlams",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)