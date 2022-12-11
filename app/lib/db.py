from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Factory:
    def __init__(self, app, SQLALCHEMY_DATABASE_URI):
        self.app = app
        self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    def make(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = self.SQLALCHEMY_DATABASE_URI
        db.init_app(self.app)
