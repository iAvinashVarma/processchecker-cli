from setuptools import setup
setup(
    name = 'processchecker-cli',
    version = '0.1.0',
    packages = ['processchecker'],
    entry_points = {
        'console_scripts': [
            'processchecker = processchecker.__main__:main'
        ]
    })