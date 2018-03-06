================
Flask Demo (WIP)
================

Just a quick example of how we could potentially start using Flask.


Organization
------------

Consider this a rough draft. Everything can be reorganized.
Maybe we don't need a `util.factories` and things like that.


Possible Improvements
---------------------

This demo will mainly use vanilla Flask with

- `flask-sqlalchemy`

- `flask-celery`

I wouldn't be surprised if `flask-restful` turns out to be useful.
That being said `flask-restless` does not seem like a strong fit


General Idea
------------

Replicate the behaviour of rhc

- 2 servers, private and public (but started at once)

- similar routing and organization (maybe use flask-restful)


Configs
-------

Flask tends to have people writing config.py files (or similar modules).
You can have something like a default that is always loaded, and then
if a production or config file is present then the defaults are overwritten.

There are a few different ways to deal with configs.


Things to Note
--------------

- Making changes in debug mode

- Handling exceptions in debug mode

Deploys
-------

Deploying in production will likely be done with uWSGI Emperor of gUnicorn.

TODO
----

- Add some basic sqlalchemy models
- Add some basically celery tasks
- Show how we might deal with async requests
- Demo what a prod deploy may look like
- Potentially dockerize

I will try to knock these out in the next week or so, depending
on how my time looks.

Potentially Useful References
-----------------------------

- https://github.com/allisson/flask-example

- https://github.com/Robpol86/Flask-Large-Application-Example/blob/master/pypi_portal/models/helpers.py
