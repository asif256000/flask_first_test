from flask import Blueprint

bp = Blueprint("auth", __name__)

from app_pkg.auth import routes
