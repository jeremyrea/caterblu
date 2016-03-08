[ ![Codeship Status for jrmrea/murmuring-fjord-45036](https://codeship.com/projects/eb4468e0-c7a2-0133-82d3-4a552c5005e4/status?branch=master)](https://codeship.com/projects/139096)
[![Coverage Status](https://coveralls.io/repos/github/jeremyrea/murmuring-fjord-45036/badge.svg?branch=master)](https://coveralls.io/github/jeremyrea/murmuring-fjord-45036?branch=master)
[![Code Health](https://landscape.io/github/jeremyrea/murmuring-fjord-45036/master/landscape.svg?style=flat)](https://landscape.io/github/jeremyrea/murmuring-fjord-45036/master)
[![Dependency Status](https://www.versioneye.com/user/projects/56de432edf573d00352c66a2/badge.svg?style=flat)](https://www.versioneye.com/user/projects/56de432edf573d00352c66a2)

# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
