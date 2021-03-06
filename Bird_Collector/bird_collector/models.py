"""SQLAlchemy models for Bird_Collector"""
from flask_sqlalchemy import SQLAlchemy 

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we pull and from which we analyze tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweets(DB.Model):
    """Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
        