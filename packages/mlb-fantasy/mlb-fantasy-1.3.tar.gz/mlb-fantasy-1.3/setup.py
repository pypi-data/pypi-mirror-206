from setuptools import setup, find_packages

setup(
    name='mlb-fantasy',
    version='1.3',
    description="MLB fantasy draft optimizer.  See README.md for more information.",
    readme = "README.md",
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
