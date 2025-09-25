# Calculator Flask App

This is a simple calculator web app implemented with `flask` and tested with `pytest`. It has unit tests which will be auto ran with Github Actions when pushing to `main` or pushing to a pull request which will be merged into `main`

## Getting Started

To run the application and tests you need to **first** install the dependencies in the `requirements.txt`. This can be done in a Python environment or globally like so:

```
pip install -r requirements.txt
```

### Running the App

To run the app just run the `app.py` file with your Python install. After this the home page of the app should be available at `localhost:5000`.

#### Running on Windows

```
python app.py
```


#### Running on Linux/MacOS

```
python3 app.py
```

### Running Tests

To run the unit tests against the app just use `pytest` to run the `test_app.py` file.

```
pytest test_app.py
```