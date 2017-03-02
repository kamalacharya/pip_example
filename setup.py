
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

long_description = \
    """An example Python package showing the ability to deploy Python packages directly
    from a git repo using pip. It shows how to include non Python files, such as
    bash scripts. It also shows how to deploy a wrapper script to /usr/local/bin without
    having to write any boilerplate code.

    This sample Python code invokes a bash script which prints the environment variables.
    """

setup(
    name='pip_example',

    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.2',

    description='pip example',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/kamalacharya/pip_example',

    # Author details
    author='Kamal Acharya',
    author_email='kamal.acharya@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Test Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='setuptools development',

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pip_example.bash_scripts': ['*.sh'],
    },

    entry_points={
        'console_scripts': [
            'pip_example = pip_example.scripts.pip_example:main',
        ],
    },
)
