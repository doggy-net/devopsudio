from setuptools import setup, find_packages


_VERSION = 0.1


setup(
    name='DevOpStudio',  # application name
    version=_VERSION,
    description="IE Resource Tool",
    long_description="IE Resource Tool for Knowledge Cloud",
    url='https://www.devopstudio.com',
    license="MIT",
    packages=find_packages(),
    include_package_data=True,  # enable manifest file
    exclude_package_data={'': ['.gitignore']},  # exclude git ignore file
)
