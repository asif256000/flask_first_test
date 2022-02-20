# Basic command required to start Heroku app
web: flask db upgrade; flask translate compile; gunicorn microblog:app
# Add below line if redis service is needed:
# worker: rq worker -u $REDIS_URL microblog-tasks