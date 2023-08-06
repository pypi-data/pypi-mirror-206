from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Package For Creating UI Elements Easier For Pygame'

setup(
    name="gui4pygame",
    version=VERSION,
    author="Shejin Shouckath",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'ui', 'gui', 'pygame'],
    )
