from app_pkg import db
from app_pkg.api import bp
from app_pkg.api.auth import basic_auth, token_auth
from flask import jsonify


@bp.route("/tokens", methods=["POST"])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({"token": token})


@bp.route("/tokens", methods=["DELETE"])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return "", 204