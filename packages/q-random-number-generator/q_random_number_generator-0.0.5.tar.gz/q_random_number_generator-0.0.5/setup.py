import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="q_random_number_generator",
    version="0.0.5",
    author="Allen Wu",
    author_email="allen91.wu@gmail.com",
    description="Using qiskit to realize random number generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allen91wu/q_random_number_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
