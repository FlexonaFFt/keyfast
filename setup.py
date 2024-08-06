from setuptools import setup, find_packages 

setup(
    name='kterm',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kterm = kterm.kterm:main',
        ],
    },
)