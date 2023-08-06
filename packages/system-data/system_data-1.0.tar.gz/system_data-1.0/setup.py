from setuptools import setup

setup(
    name='system_data',
    version='1.0',
    description='A Python module that fetches system data and utilities.',
    author='Ahson Shaikh',
    author_email='ahsonshaikh616@gmail.com',
    packages=['system_data'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'system=system_data.system_data:main'
        ]
    }
)
