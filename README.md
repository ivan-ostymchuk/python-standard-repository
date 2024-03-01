# Python Standard Repository

This is the standard repository I use for my Python projects. It has all the tools that a python repository should have to make you
more productive and to avoid all the different problems you might face with Python.
Depending on the project I might add or remove some of the checks but the main idea is:
- Use type hints
- Use mypy to check type consistency and correctness
- Check code security
- Automate formatting
- Check docstring format if present
- Use unit tests
- Use integration tests

The goals are:

- Easy environment reproducibility, setup and maintainability.   
- Automated code formatting and checks.   
- Mandatory code checks, unit tests and integration tests on Pull Request  

Tools implemented:
- Poetry for dependency management (packages and their versions defined in a toml file).   
  Dependency groups can be specified, each group with its own packages (per environment or purpose)
- Pre-commit library for the checks. To automatically format code and execute all the checks and unit tests before each commit.
- A bash script that executes all the commands to set up the environment (Install poetry and pre-commit)
- CI-CD pipelines in yaml files that will be executed on every Pull Request on Github   
  With the same checks that were previously executed by pre-commit and integration tests.

# Environment setup locally

The environment manager used is poetry, if you don't have it the bash script will install it for you.
To setup the environment run:

- sh scripts/poetry_init.sh -> to install all the dependencies

# Environment setup on a server (cloud or on-prem)

Install the requirements.txt file which is automatically maintained and versioned by poetry and pre-commit during development.

# Pre-commit checks

Tha yaml file contains the configuration for pre-commit checks and formatting.  
If some of the checks fail the commit will not be pushed.  
When the code formatting is modified by pre-commit hooks you have to stage again the files modified.

If you want to perform all the checks on your code before committing, run in the terminal:

- pre-commit run --all-files
