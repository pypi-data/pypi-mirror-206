from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mlb-fantasy',
    version='1.4',
    description="MLB fantasy draft optimizer.  See README.md for more information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'sklearn',
        'pulp',
        'matplotlib',
        'seaborn',
    ],
    entry_points={
        'console_scripts': [
            'mlb-fantasy=mlb_fantasy.main:main',
        ],
    },
)
