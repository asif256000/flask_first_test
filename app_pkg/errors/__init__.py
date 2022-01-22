from flask import Blueprint

bp = Blueprint("errors", __name__)

from app_pkg.errors import handlers
