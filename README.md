# dkany
Python package for accessing open data websites powered by dkan

# Local Development

To install the package and it's dependences for development, run 
```
pipenv install --dev
```
Pipenv may sometimes have difficulty finding the specific version of python on your system, so you'll have to point it to the version of python. It's possible to use pyenv-win to manage versions of python https://github.com/pyenv-win/pyenv-win
```
pyenv install -l 
pyenv install 3.9.6
```

You can point pipenv to a specific python version manually by adding the --python option, for example 
```
pipenv install --dev --python C:/Users/pmariani/.pyenv/pyenv-win/versions/3.9.6/python.exe
```


## Environment Variables
 The default behavior of this app can be changed with environment variables.
 The easiest way to set these is by adding them to a `.env` file in the base directory of this repo. This file is not commited to the repo, as it might change in different contexts, but you can see the `.env_example` to get a sense of how this might look.

Here are the environment variables the app is currently using:

# Running the Tests
There are many ways to run the tests associated with this app.

1. Probably the easiest is to run the tests in vscode's testing pannel

2. You can also run the tests from bash with `source scripts/test.sh` 


# Ideas for Improvement
TODO: Validate dataset file (All columns have column names)

# Deploying

See [our confluence doc on deploying to AWS CodeArtifact](https://mathematicampr.atlassian.net/wiki/spaces/WEB/pages/2514354711/Deploying+to+AWS+CodeArtifact)