from setuptools import setup, find_packages


setup(
    # include_package_data=True,
    name='jpd',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        '': ['*.txt', '*.json']
    },
    entry_points={
        'console_scripts': [
            'jpd=main:jpd'
        ]}
)

