[![Build Status](https://travis-ci.org/jeremyrea/caterblu.svg?branch=master)](https://travis-ci.org/jeremyrea/caterblu)
[![Coverage Status](https://coveralls.io/repos/github/jeremyrea/caterblu/badge.svg?branch=master)](https://coveralls.io/github/jeremyrea/caterblu?branch=master)
[![Code Health](https://landscape.io/github/jeremyrea/caterblu/master/landscape.svg?style=flat)](https://landscape.io/github/jeremyrea/caterblu/master)
[![Dependency Status](https://www.versioneye.com/user/projects/56e03ea9df573d00352c68e3/badge.svg?style=flat)](https://www.versioneye.com/user/projects/56e03ea9df573d00352c68e3)

# caterblu

A Django project to retrieve various informations on blu-ray releases.

## Running Locally

Make sure you have the latest stable version of `Python3` with `pip` on your system.

This project also uses `Bower` for front-end dependency management. Follow the [installation instructions](http://bower.io/#install-bower) to get set up.

Then follow these steps:

```sh
$ git clone git@github.com:jeremyrea/caterblu.git
$ cd caterblu

$ virtualenv venv
$ source venv/bin/activate

$ pip install -r requirements.txt
$ python3 manage.py bower -v 0 install

$ python3 manage.py collectstatic --no-input
$ gunicorn caterblu.wsgi
```

The app should now be running on [localhost:8000](http://localhost:8000/).

You will also have to supply `AWS_ACCESS_KEY_ID`, `AWS_ASSOCIATES_TAG`, `AWS_SECRET_ACCESS_KEY` in your environment variables in order to retrieve pricing information from AmazonAPI and a Django `SECRET_KEY`.

## Tests

You can run the tests with:
```sh
$ nose2 -v
```
