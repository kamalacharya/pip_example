# pip_example

This is an example Python package showing the ability to install and upgrade Python packages
directly from a GitHub repo using pip. It shows how to include non Python files, such as bash
scripts. It also shows how to deploy a wrapper script to /usr/local/bin (or any other system
dependent paths) without having to write any boilerplate code.

**This code has been tested on Python 2.7**.

This sample Python code invokes a bash script which just prints the environment variables.

To install pip_example:
`pip install git+https://github.com/kamalacharya/pip_example.git#egg=pip_example`

To upgrade to the latest version on GitHub:
`pip install --upgrade git+https://github.com/kamalacharya/pip_example.git#egg=pip_example`

To uninstall pip_example:
`pip uninstall pip_example`
