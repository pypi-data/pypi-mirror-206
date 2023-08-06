from setuptools import setup, find_packages

setup(
    name='mlb-fantasy',
    version='1.2',
    description="MLB fantasy draft optimizer.  Requires a draft_picks.txt file with the format: 'Player Name: Team 1, Team 2, Team 3, Team 4, Team 5, Team 6' with each player picks on a new line.",
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
