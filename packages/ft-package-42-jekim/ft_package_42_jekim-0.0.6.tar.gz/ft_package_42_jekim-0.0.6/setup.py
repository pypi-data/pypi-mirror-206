import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.0.6"
SUMMARY = "A small example package"

setuptools.setup(
    name="ft_package_42_jekim",
    version=VERSION,
    author="Two-Jay",
    author_email="djeeee1272@gmail.com",
    license="MIT",
    description=SUMMARY,
    long_description=long_description,
    url="https://github.com/Two-Jay/42_Python_for_DataScience",
    packages=setuptools.find_packages('ft_package_42_jekim'),
)

# how to install:

# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade setuptools
# python3 -m pip install --upgrade wheel
# python3 -m pip install --upgrade twine

# python3 setup.py sdist bdist_wheel

# python -m twine upload dist/*

# then you can install it with 'pip install ft_package_42_jekim'