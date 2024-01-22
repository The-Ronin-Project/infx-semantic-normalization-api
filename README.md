# infx-internal-tools
![Generic badge](https://img.shields.io/badge/python-3.9-blue)
![Generic badge](https://img.shields.io/badge/code%20style-black-000000.svg)


> Note: This readme was copied from infx-internal-tools and still needs some clean up and fine-tuning


## Team Conventions
### Branch naming

Our basic convention is INFX-{ticket-number}-lower-case-identifier

### Project Setup

This project managed by Poetry.

Use [Pipx](https://github.com/pypa/pipx) to install it.
```bash
pipx install poetry
```
For more information, read [the docs](https://python-poetry.org/docs/)

### Python Versions and Virtualenvs

The version is controlled in the [pyproject.toml](pyproject.toml) `tool.poetry.dependencies` section.

To create/use a virtual env, run
```bash
poetry shell
```
If you don't have the required Python version installed locally, use PyEnv to download it.

### Install pyenv

`brew install pyenv`

Load pyenv automatically by appending
the following to ~/.zshrc:

open .zshrc using `open ~/.zshrc`

If the file does not already exist, create it using `touch ~/.zshrc`

Then append the following line to the end of the file.

`eval "$(pyenv init -)"`

To list the all available versions of Python, including Anaconda, Jython, pypy, and stackless, use:
`$ pyenv install --list`

Then install the desired versions:
```
$ pyenv install 3.9.10
$ pyenv versions
```

The [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) plugin can be used to manage virtualenvs.

`brew install pyenv-virtualenv`

Load pyenv virtualenv automatically by appending
the following to the end of  ~/.zshrc:

`eval "$(pyenv virtualenv-init -)"`

To create a virtualenv for the Python version used with pyenv, run pyenv virtualenv, specifying the Python version you are using and the name of the virtualenv directory. For example,

`$ pyenv virtualenv 3.9.10 infx-internal-tools`

If eval "$(pyenv virtualenv-init -)" is configured in your shell, pyenv-virtualenv will automatically activate/deactivate virtualenvs on entering/leaving directories which contain a .python-version file that contains the name of a valid virtual environment as shown in the output of pyenv virtualenvs (e.g., venv34 or 3.4.3/envs/venv34 in example above) . .python-version files are used by pyenv to denote local Python versions and can be created and deleted with the pyenv local command.

You can also activate and deactivate a pyenv virtualenv manually:

`pyenv activate <name>`
`pyenv deactivate`

virtualenv should work fine with pipenv


### Setting up a dev environment

#### Tool set
- Docker Desktop
- Git (can be installed via xcode command line tools, or use GitHub Desktop)
- PyCharm IDE
- pgAdmin
- Postman 
- Homebrew (https://brew.sh)


#### PyCharm setup
1. In PyCharm, open the project. The later versions of PyCharm should recognize it as a Poetry project


#### Flask setup: Run and Debug in PyCharm
1. In PyCharm, open [app/app.py](app/app.py)
2. At top right, near the Run and Debug icons, drop the menu and choose `Edit configuration`
3. Modify the Flask server configuration in this dialog:
    - Name: Flask
    - Target type: Script path
    - Target: (navigate to the local file infx-internal-tools/app/app.py)
    - Application: application
    - Additional options: `--host=0.0.0.0 --port=5500` (See note on port below.)
    - FLASK_ENV: development
    - FLASK_DEBUG: (check the box)
    - Python interpreter: (should already be correct from "PyCharm setup" above)
    - Working directory: (navigate to local folder infx-internal-tools)
    - Add content/source roots to PYTHONPATH (check both boxes)
4. Choose Apply and OK. 
5. Restart PyCharm

> Note that the Postman `Dev-Local` environment uses port 5000 as the initial value. However, [port 5000 is used by the AirPlay
> Receiver service on Macbooks](https://developer.apple.com/forums/thread/682332) and may block the application from
> running locally. Alteration of port configurations may be necessary for local testing.

#### Running from the command line

Install dependencies
```bash
poetry install
```


### Running a dev server

#### PyCharm
1. In PyCharm, working in the infx-internal-tools repo, open a terminal session.
2. In the terminal session, activate your environment by name: `pyenv activate infx-internal-tools`
3. Environment is active when you see that name at the start of the terminal prompt: `(infx-internal-tools) `
4. If dependencies and/or the [Pipfile](Pipfile) have changed recently, also run: `pipenv install --dev`
5. Either:
    - In the terminal session, enter: `python -m app.app` to start the local dev server, or: 
    - At top right in the PyCharm window, near the Run and Debug icons, select Flask and click either Run or Debug to start the server.
6. In the terminal console, see messages that Debug mode is on and the Debugger is active. 
8. In Postman, in the Informatics workspace, choose your working environment:
    - `Dev-Local` to run the code in your local environment:
    - `Prod` to run the code currently deployed in Prod
    - `Dev` to run the code currently deployed in Dev
    - `Dev-Docker` to run the Docker image in your local machine environment
9. Then run test calls in Postman.
10. If you started Flask with Debug, in the PyCharm window you can step through the code running in your virtual environment. 
10. Postman will display messages when there are issues. In Prod, [DataDog](https://app.datadoghq.com/logs) also displays messages. 
11. To debug Dev or Prod, first setup your local virtual environment to use a branch that is synchronized with the deployed code in Dev or Prod, then debug.
12. When using Postman, if the API request is calling to RxNav-in-a-box, make sure that container is running in Docker first.

#### CLI
```bash
poetry run flask --app infx_mapping.app.app  run
```


### Testing

POC quick test:
```bash
curl localhost:5000/ping
```

We use [Pytest](https://docs.pytest.org/en/6.2.x/) for automated testing, Postman for manual testing.

We  split integration tests and unit tests into separate directories. Code coverage should be calculated using integration tests. 

Tests are in folders outside the app at the top level of the project. Pytest will discover them. 


### Project Structure

Modified frequently:
- [app](app) - Python application - API endpoints - model-view-controller
- [test](test) - Python unit tests and supporting JSON data files
- [integration_tests](integration_tests) - SQL integration tests

Occasional changes:
- [.github](.github) - GitHub CI/CD workflows
- Top level project configuration files - [docker-compose.yml](docker-compose.yml), [pull_request_templaet.md](pull_request_templaet.md), [codecov.yml](codecov.yml), [Pipfile](Pipfile), etc.
