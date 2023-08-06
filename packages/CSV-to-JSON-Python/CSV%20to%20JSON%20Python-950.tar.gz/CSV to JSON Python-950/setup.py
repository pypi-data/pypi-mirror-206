import setuptools
import hashlib
import random
import time

def randon_number_generator():
    rand_num = random.getrandbits(128)
    timestamp = int(time.time())

    # Concatenate the random number and timestamp as input to the hash function
    input_str = str(rand_num) + str(timestamp)

    # Hash the input string using SHA-256
    hash_obj = hashlib.sha256(input_str.encode('utf-8'))

    # Get the hash value as a hexadecimal string
    hash_str = hash_obj.hexdigest()

    # Convert the hash value to an integer between 0 and 1000
    random_value = int(hash_str, 16) % 1000
    return random_value


version_number = randon_number_generator()

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "CSV to JSON Python",
    version = version_number,
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