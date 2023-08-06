from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="emoji-generator",
    version="0.7",
    packages=find_packages(),
    install_requires=[],
    description="A package for working with smiley emojis",
    author="codethreads",
    author_email="bellamyy.blakee100@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
