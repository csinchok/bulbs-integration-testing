# Bulbs CMS Reference

This repo is used for integration testing, etc. Making sure that our Python and JS libraries work together properly.

## Setup:

    $ virtualenv .
    $ source ./bin/activate
    $ npm install
    $ bower install
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py synces 0001
    $ python manage.py es_swap_aliases 0001
    $ python manage.py make_test_tokens
    $ python manage.py runserver 