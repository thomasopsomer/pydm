from setuptools import setup, find_packages

__version__ = "0.2.1"

install_requires = [
    'docker-py',
]

setup(
    name="dockermachinepy",
    version=__version__,
    packages=find_packages(),
    install_requires=install_requires,
    package_data={
        '': ['*.rst'],
    },
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Python wrapper around docker-machine",
    license="GPL2",
    keywords="docker machine docker-machine container",
    url="https://github.com/thomasopsomer/pydm"
)
