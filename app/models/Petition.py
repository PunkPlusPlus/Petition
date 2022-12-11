from app.lib.db import db


class Petition(db.Model):
    __tablename__ = 'Petitions'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer)
    body = db.Column(db.String)
    title = db.Column(db.String)
    level = db.Column(db.Integer)
    approves = db.Column(db.Integer)
    creator_id = db.Column(db.Integer)
