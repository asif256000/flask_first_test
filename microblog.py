from app_pkg import create_app, db, mail, cli
from app_pkg.models import User, Post


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Mail': mail}

