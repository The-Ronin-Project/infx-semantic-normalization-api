# infx-semantic-normalization-api
![Generic badge](https://img.shields.io/badge/python-3.11-blue)
![Generic badge](https://img.shields.io/badge/code%20style-black-000000.svg)

INFX Semantic Normalization Service. Implements service for code mapping.

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
poetry env use 3.11.7
poetry shell
```
If you don't have the required Python version installed locally, use PyEnv to download and activate it.
```bash
pyenv install 3.11.7
pyenv <scope> 3.11.7
```
[Read here](https://github.com/projectronin/infx-internal-tools?tab=readme-ov-file#install-pyenv) if you need more information on PyEnv.

### Setting up a dev environment

#### Tool set
- Docker Desktop
- Git (can be installed via xcode command line tools, or use GitHub Desktop)
- PyCharm IDE
- Postman


#### PyCharm setup
1. In PyCharm, open the project. The later versions of PyCharm should recognize it as a Poetry project
2. Select the correct Python interpreter (likely your virtual env). Click the Python version in the lower right corner
of the PyCharm window.


#### Flask setup: Run and Debug in PyCharm
1. In PyCharm, open [infx_semantic_normalization_api/app.py](infx_semantic_normalization_api/app.py)
2. At top right, near the Run and Debug icons, drop the menu and choose `Edit configuration`
3. Modify the Flask server configuration in this dialog:
    - Name: Flask
    - Target type: Script path
    - Target: (navigate to the local file infx-semantic-normalization-api/app/app.py)
    - Application: application
    - Additional options: `--host=0.0.0.0 --port=5500`
    - FLASK_ENV: development
    - FLASK_DEBUG: (check the box)
    - Python interpreter: (should already be correct from "PyCharm setup" above)
    - Working directory: (navigate to local folder infx-semantic-normalization-api)
    - Add content/source roots to PYTHONPATH (check both boxes)
4. Choose Apply and OK. 


#### Running from the command line

Install dependencies
```bash
poetry install
```

### Running a dev server

1. In the terminal session, activate your environment by: `poetry shell`
1. Environment is active when you see that name at the start of the terminal prompt: e.g. `(infx-semantic-normalization-api-py3.11) `
1. If dependencies have changed recently, also run: `poetry install`
1. Either:
    - In the terminal session, enter: `poetry run python -m infx_semantic_normalization_api.app` to start the local dev server, or:
      - Note that when running from the CLI, you cannot specify the service port (unless you update the param in the `application.run`
        call in [the code](infx_semantic_normalization_api/app.py)).
    - At top right in the PyCharm window, near the Run and Debug icons, select Flask and click either Run or Debug to start the server.
1. In the terminal console, see messages that Debug mode is on and the Debugger is active.
1. In Postman, in the Informatics workspace, choose your working environment:
   - `Dev-Local` to run the code in your local environment:
   - `Prod` to run the code currently deployed in Prod
   - `Dev` to run the code currently deployed in Dev
   - `Dev-Docker` to run the Docker image in your local machine environment
1. Then run test calls in Postman.
1. If you started Flask with Debug, in the PyCharm window you can step through the code running in your virtual environment.
1. Postman will display messages when there are issues. In Prod, [DataDog](https://app.datadoghq.com/logs) also displays messages.
1. To debug Dev or Prod, first set up your local virtual environment to use a branch that is synchronized with the deployed code in Dev or Prod, then debug.
1. When using Postman, if the API request is calling to RxNav-in-a-box, make sure that container is running in Docker first.



### Testing

POC quick test:
```bash
curl localhost:5500/ping
```

We use [Pytest](https://docs.pytest.org/en/6.2.x/) for automated testing, Postman for manual testing.
* Run automated tests
  ```bash
  poetry run pytest
  ```

#### Local Container Testing
* Build the docker image
  ```bash
  docker build . -t infx-semantic-normalization-api
  ```
* Run the container
  * Docker
    ```bash
      docker run -d -p 127.0.0.1:8000:8000 infx-semantic-normalization-api
    ```
  * Docker compose
    ```bash
      docker compose up -d
    ```
* Test the container
  * Use postman to run a GET against `localhost:8000/ping` or
    ```bash
    curl localhost:8000/ping
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

