from app_pkg import cli, create_app, db, mail
from app_pkg.models import Message, Notification, Post, User

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Mail": mail,
        "User": User,
        "Post": Post,
        "Message": Message,
        "Notification": Notification,
    }
