import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="PyOblv",
    version="0.2.2",
    description="A client library for accessing Oblivious APIs. PyOblv is now deprecated, and will not be supported in future. Kindly use [oblv-ctl](https://pypi.org/project/oblv-ctl/) to access Oblivious APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Oblivious',
    author_email='hello@oblivious.ai',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ], 
    keywords='Oblivious python package',
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["httpx >= 0.15.0, < 0.24.0",
                      "attrs >= 21.3.0", 
                      "python-dateutil >= 2.8.0, < 3",
                      "jsonschema >= 4.1.1", 
                      "typer >= 0.7.0",
                      "rich >= 11.2.0",
                      "requests"],
    package_data={"oblv": ["py.typed"]},
    entry_points={
        "console_scripts": ["oblv-ctl = cli.main:app"],
    }
)
