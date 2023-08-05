import io
from setuptools import (
    setup,
    find_packages,
)  # pylint: disable=no-name-in-module,import-error


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


with io.open("README.md", encoding="utf-8") as infile:
    long_description = infile.read()

setup(
    name="gyrate",
    packages=find_packages(exclude=("ext", "examples")),
    version="0.0.32",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.8",
    description="create beautiful and elegant terminal spinners",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "console",
        "spinner",
        "loading",
        "cli",
        "spinners",
        "terminal"
    ],
    install_requires=dependencies("requirements.txt"),
    tests_require=dependencies("requirements-dev.txt"),
    include_package_data=True,
    extras_require={"ipython": ["IPython==5.7.0", "ipywidgets==7.1.0",]},
)
