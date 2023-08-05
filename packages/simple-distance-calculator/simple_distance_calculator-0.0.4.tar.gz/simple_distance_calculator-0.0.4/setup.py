from setuptools import setup, find_packages

setup(
    name='simple_distance_calculator',
    version='0.0.4',
    author='Aivcho',
    author_email='achomskis@gmail.com',
    description='A distance calculator',
    long_description=open('README.txt', encoding='utf-8').read(),
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)