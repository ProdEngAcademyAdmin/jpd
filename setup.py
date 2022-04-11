from setuptools import setup, find_packages


setup(
    name='jpd',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jpd = src.main:cli'
        ]}
)

