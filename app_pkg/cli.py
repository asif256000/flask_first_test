import os

import click


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument("lang")
    def init(lang):
        """Initialize a new language.e.g: flask translate init <LANG CODE>"""
        if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
            raise RuntimeError("extract command failed")
        if os.system(r"pybabel init -i messages.pot -d app_pkg\translations -l " + lang):
            raise RuntimeError("init command failed")
        os.remove("messages.pot")

    @translate.command()
    def update():
        """Update all languages.e.g: flask translate update"""
        if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
            raise RuntimeError("extract command failed")
        if os.system(r"pybabel update -i messages.pot -d app_pkg\translations"):
            raise RuntimeError("update command failed")
        os.remove("messages.pot")

    @translate.command()
    def compile():
        """Compile all languages.e.g: flask translate compile"""
        if os.system(r"pybabel compile -d app_pkg\translations"):
            raise RuntimeError("compile command failed")
