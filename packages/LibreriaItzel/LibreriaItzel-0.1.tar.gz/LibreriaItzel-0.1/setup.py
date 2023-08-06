import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.1'
PACKAGE_NAME = 'LibreriaItzel'
AUTHOR = 'Itzel Franco'
AUTHOR_EMAIL = 'itzel_fd1@tesch.edu.mx'
URL = 'https://github.com/itzelfd98'

LICENSE = 'MIT'
DESCRIPTION = 'libreria de nombres de mujer y hombre'

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'pandas'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)