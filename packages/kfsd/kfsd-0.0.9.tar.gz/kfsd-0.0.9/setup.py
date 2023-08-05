from setuptools import setup, find_packages

setup(
    name='kfsd',
    version='0.0.9',
    description='Sample App',
    long_description='Sample Pkg',
    long_description_content_type="text/markdown",
    author='Gokul Nathan',
    author_email='nathangokul111@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==4.1.6',
        'asgiref==3.6.0',
        'coverage==7.1.0',
        'djangorestframework==3.13.1',
        'flake8==6.0.0',
        'mccabe==0.7.0',
        'netifaces==0.11.0',
        'pycodestyle==2.10.0',
        'pyflakes==3.0.1',
        'pytz==2022.7.1',
        'PyYAML==6.0',
        'sqlparse==0.4.3',
        'drf-spectacular==0.22.1',
        'ruamel.yaml==0.17.21',
        'requests==2.28.2'
    ],
)
