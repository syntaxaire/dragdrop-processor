# Easily process drag-and-dropped files
This simple project will serve a static page with a drop target. Dropping
any files here will upload them to the backend Flask app for processing.

The purpose of this is to act as an extensible base for general file
processing projects. Although a webapp adds infrastructure overhead,
it is easier for a user to understand and access.

# Running
```
python -m pip install pipenv
pipenv sync
pipenv run start
```
