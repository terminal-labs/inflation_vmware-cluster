import sys
from setuptools import setup, find_packages

assert sys.version_info >= (3, 6, 0)

VERSION = "0.0.1"

setup(
    name="vmwarecluster",
    version=VERSION,
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="see LICENSE file",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git@master#egg=utilitiespackage&subdirectory=utilitiespackage",
        "keyloader@git+https://gitlab.com/terminallabs/experimental-tools/python_key-loader.git@master#egg=keyloader&subdirectory=keyloader",
        "apiwrapper@git+https://gitlab.com/terminallabs/experimental-tools/python_api-wrapper.git@master#egg=apiwrapper&subdirectory=apiwrapper",
        "rambo-vagrant",
    ],
    entry_points="""
        [console_scripts]
        vmwarecluster=vmwarecluster.cli:main
     """,
)
