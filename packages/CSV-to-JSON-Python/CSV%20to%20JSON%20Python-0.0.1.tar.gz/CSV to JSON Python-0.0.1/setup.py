import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CSV to JSON Python",
    version = "0.0.1",
    author = "Paul Ndambo",
    author_email = "paulkadabo@gmail.com",
    description = "This is a package used to convert csv data to a json object",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://testpypi.org/project/CSV to JSON Python/",
    project_urls = {
        "Bug Tracker": "https://testpypi.org/project/CSV to JSON Python/",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)