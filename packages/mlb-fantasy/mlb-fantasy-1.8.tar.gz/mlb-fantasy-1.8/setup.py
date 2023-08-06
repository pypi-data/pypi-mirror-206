from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='mlb-fantasy',
    version='1.8',
    description="MLB fantasy draft optimizer.  See README.md for more information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pybaseball==2.2.5',
        'openpyxl==3.1.2',
    ],
    entry_points={
        'console_scripts': [
            'mlb-fantasy=mlb_fantasy.main:main',
        ],
    },
)
