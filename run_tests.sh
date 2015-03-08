#!/usr/bin/env bash

# Do we need to create fixtures?
if [ ! -f cache.sqlite3 ]
	then
	./cache_fixtures.sh
fi

# Load the fixtures
cp cache.sqlite3 db.sqlite3
python manage.py synces 0001
python manage.py es_swap_aliases 0001
python manage.py bulk_index

# Fork the django server
uwsgi --http=localhost:8000 --module=integration.wsgi:application --home=$PWD --master -d ./uwsgi.log --pidfile=./uwsgi.pid

karma start karma.conf.js

kill -SIGINT $(cat ./uwsgi.pid)
rm ./uwsgi.pid
rm ./uwsgi.log
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_tag_0001
curl -XDELETE http://127.0.0.1:9200/dbsqlite3_content_content_0001