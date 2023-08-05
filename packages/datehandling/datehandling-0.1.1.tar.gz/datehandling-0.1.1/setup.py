from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name="datehandling",
      version="0.1.1",
      author="Daniel Chaparro",
      author_email="daniel.chaparro.ds@gmail.com",
      description="library for handling dates",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="",
      )