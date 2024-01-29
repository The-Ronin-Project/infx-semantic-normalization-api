# infx-mapping
![Generic badge](https://img.shields.io/badge/python-3.9-blue)
![Generic badge](https://img.shields.io/badge/code%20style-black-000000.svg)

INFX Mapping Service. Implements a REST API for code mapping

> Note: This readme was copied from [infx-internal-tools](https://github.com/projectronin/infx-internal-tools) and
> still needs some clean up and fine-tuning


## Team Conventions
### Branch naming

Our basic convention is INFX-{ticket-number}-lower-case-identifier

### Project Setup

This project is managed by [Poetry](https://python-poetry.org/).

Use [Pipx](https://github.com/pypa/pipx) to install Poetry.
```bash
brew install pipx
pipx ensurepath
```

```bash
pipx install poetry
```
For more information, read [the docs](https://python-poetry.org/docs/)

### Python Versions and Virtualenvs

The version is controlled in the [pyproject.toml](pyproject.toml), `tool.poetry.dependencies` section.

To create/use a virtual env, run
```bash
poetry env use 3.9.10
```
If you don't have the required Python version installed locally, use PyEnv to download and activate it.
[Read here](https://github.com/projectronin/infx-internal-tools?tab=readme-ov-file#install-pyenv) if you need more information on PyEnv.

### Setting up a dev environment

#### Tool set
- Docker Desktop
- Git (can be installed via xcode command line tools, or use GitHub Desktop)
- PyCharm IDE
- Postman


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

> Note that the Postman `Dev-Local` environment uses port 5000 as the initial value. However,
> [port 5000 is used by the AirPlay Receiver service on Macbooks](https://developer.apple.com/forums/thread/682332)
> and may block the application from running locally. Alteration of port configurations may be necessary for local testing.

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
poetry run flask --app infx_mapping.app.app run
```


### Testing

POC quick test:
```bash
curl localhost:5000/ping
```

We use [Pytest](https://docs.pytest.org/en/6.2.x/) for automated testing, Postman for manual testing.

#### Local Container Testing
* Build the docker image
  ```bash
  docker build . -t infx-mapping
  ```
* Run the container
  * Docker
    ```bash
      docker run -d -p 127.0.0.1:5000:5000 infx-mapping
    ```
  * Docker compose
    ```bash
      docker compose up -d
    ```
* Test the container
  * Use postman to run a GET against `localhost:5000/ping` or
    ```bash
    curl localhost:5000/ping
    ```
* Stop the container
  * Docker
    ```bash
    docker kill <container id>
    ```
    You can get the container id from running `docker ps`
  * Docker compose
    ```bash
    docker comopose down
    ```






