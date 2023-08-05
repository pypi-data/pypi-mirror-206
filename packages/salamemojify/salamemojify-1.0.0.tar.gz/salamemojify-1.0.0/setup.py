import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="salamemojify",
    version="1.0.0",
    license="MIT",
    scripts=["salamemojify", "salamemojify.py", "test_salamemojify"],
    author="salammzere3",
    author_email="salamhunter@hotmail.com",
    description="Obfuscate your python script by converting it to emoji icons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://t.me/T5B55",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
