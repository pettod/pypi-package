from setuptools import setup
from package_name import __version__


setup(
    name="package_name",
    version=__version__,
    description="Python test package",
    url="github/url/to/repository",
    packages=["package_name"],
    install_requires=open("requirements.txt").read().splitlines(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)