from setuptools import setup, find_packages

setup(
    name='my_common_response',
    version='0.1',
    description='Common response package for Django',
    author='Praveen Dhakad',
    author_email='praveendhakad97@gmail.com.com',
    url='https://github.com/parv06',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
)
