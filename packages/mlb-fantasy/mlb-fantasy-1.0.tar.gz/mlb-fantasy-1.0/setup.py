from setuptools import setup, find_packages

setup(
    name='mlb-fantasy',
    version='1.0',
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
