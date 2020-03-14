# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="lambdata_pkg_danoand1",
    version="1.0",
    author="Dan Anderson",
    author_email="danfanderson@gmail.com",
    description="For learning purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    # license="MIT",
    url="https://github.com/danoand/lambdata-pkg-danoand",
    # keywords="",
    packages=find_packages()
)
