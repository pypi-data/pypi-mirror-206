import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft_package_42_jekim",
    version="0.0.1",
    author="Two-Jay",
    author_email="djeeee1272@gmail.com",
    license="MIT",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/Two-Jay/42_Python_for_DataScience",
    packages=setuptools.find_packages(),
)