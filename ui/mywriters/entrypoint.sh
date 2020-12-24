#!/bin/bash
set -e

case "$1" in
    migrate)
        exec python manage.py migrate
    ;;
    serve)
        exec gunicorn mywriters.wsgi
    ;;
    check-feeds)
        exec python manage.py check_feeds --read
    ;;
    *)
        exec "$@"
    ;;
esac
        


