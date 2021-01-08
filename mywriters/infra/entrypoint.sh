#!/bin/bash
set -e

case "$1" in
    migrate)
        exec python manage.py migrate
    ;;
    serve)
        exec gunicorn mywriters.wsgi
    ;;
    serve-local)
        exec python manage.py runserver 0.0.0.0:$PORT
    ;;
    generate-feeds)
        exec python manage.py generate_feeds
    ;;
    *)
        exec "$@"
    ;;
esac
        


