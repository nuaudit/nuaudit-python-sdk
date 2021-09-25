from setuptools import setup, find_packages

NAME = "nuaudit_python_sdk"
VERSION = "0.17.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    install_requires=[
        "nuaudit-python-autogen==0.17.0",
        "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "urllib3==1.26.7; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4' and python_version < '4'",
    ],
    name=NAME,
    version=VERSION,
    description="Nuaudit",
    license="MIT",
    author="Nuaudit Support",
    author_email="support@nuaudit.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nuaudit/nuaudit-python-sdk",
    packages=find_packages(exclude=["test", "tests"]),
    project_urls={
        "Bug Tracker": "https://github.com/nuaudit/nuaudit-python-sdk/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
