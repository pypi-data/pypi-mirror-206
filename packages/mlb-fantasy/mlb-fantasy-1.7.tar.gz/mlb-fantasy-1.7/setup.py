from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='mlb-fantasy',
    version='1.7',
    description="MLB fantasy draft optimizer.  See README.md for more information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'mlb-fantasy=mlb_fantasy.main:main',
        ],
    },
)
