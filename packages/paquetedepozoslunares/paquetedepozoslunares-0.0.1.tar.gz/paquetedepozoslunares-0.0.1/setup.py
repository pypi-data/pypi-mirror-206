import setuptools
from pathlib import Path


long_desc = Path("README").read_text()

setuptools.setup(
       name="paquetedepozoslunares",
       version="0.0.1",
       long_description=long_desc,
       packages=setuptools.find_packages( exclude="caca")

)