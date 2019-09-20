from setuptools import setup, find_packages


_VERSION = 0.1


setup(
    name='DevOpStudio',  # application name
    version=_VERSION,
    url='https://www.devopstudio.com',
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,  # enable manifest file
    exclude_package_data={'': ['.gitignore']},  # exclude git ignore file
)
