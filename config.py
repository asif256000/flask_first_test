import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        if db_url.startswith("postgres"):
            db_url = db_url.replace("postgres://", "postgresql://")
    else:
        db_url = "sqlite:///" + os.path.join(basedir, "app_pkg.db")
    # .replace('postgres://', 'postgresql://') -> with DATABASE_URL in case of HEROKU Deployment, to use Postgresql
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get("REDIS_URL") or "redis://"

    POSTS_PER_PAGE = 5
    LANGUAGES = ["en", "es", "bn", "hi"]

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_API_KEY")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    ADMINS = ["asif256000@gmail.com"]

    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY")
    GOOGLE_TRANSLATOR_KEY = os.environ.get("GOOGLE_TRANSLATOR_KEY")

    ELASTICSEARCH_URL = os.environ.get("ELASTICSEARCH_URL")

    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
