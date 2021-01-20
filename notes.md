# Using Poetry

## Method 1 | toml.poetry.scripts

In the app.py, if I have a function called `main` and I reference this in the pyproject.toml file:
```toml
[tool.poetry.scripts]
flask-poetry-example = "flask_poetry_example.app:main"
```

Then I don't need any environment variables, e.g. `FLASK_APP` and I can just do this:
```bash
poetry install
poetry run flask-poetry-example
```

The `app.py` has a `main` function which does this

```python
def main():
    app = create_app()
    app.run()

```


## Method 2 | flask run

Without the main function and without the `poetry run flask-poetry-example` code.

The set the `FLASK_APP` and (optionally) the `FLASK_ENV` environment variables:

```bash
export FLASK_APP=flask_poetry_example.app
poetry install
poetry run flask run
```

It does not seem to care about the `src` directory, and then it finds the `flask_poetry_example` directory (module) and the `app.py` file.

This blog on Twilio is useful:
https://www.twilio.com/blog/how-run-flask-application


# Using gunicorn

## Method 1

It looks like when you are using the `application factory` pattern, you can just call the `create_app()` function directly from the command line.

```bash
poetry run gunicorn -w 4 "flask_poetry_example:create_app()"
```

## Method 2

You can also specify another python file which loads the app, e.g. `wsgi.py`. Start it by doing this:
```bash
poetry run gunicorn -w 4 "flask_poetry_example.wsgi:app"
```
```python
# src/flask_poetry_eample/wsgi.py
from .app import create_app

app = create_app()
```

https://stackoverflow.com/questions/25319690/how-do-i-run-a-flask-app-in-gunicorn-if-i-used-the-application-factory-pattern
