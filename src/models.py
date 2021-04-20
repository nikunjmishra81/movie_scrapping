from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Scrapping(BaseModel, db.Model):
    """Model for the Scrapping table"""
    __tablename__ = 'txn_scrapped_data'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(5000),index=False,
        unique=False, nullable=True)
    rating = db.Column(db.String(500),index=False,
        unique=False, nullable=True)
    director = db.Column(db.String(500),index=False,
        unique=False, nullable=True)
    actors = db.Column(db.String(500), index=False,
        unique=False,nullable=True)
    genre = db.Column(db.String(500),index=False,
        unique=False, nullable=True)
    runtime = db.Column(db.String(500),index=False,
        unique=False, nullable=True)
    url = db.Column(db.String(500), index=False,
        unique=False,nullable=True)
    type = db.Column(db.String(500), index=False,
        unique=False,nullable=True)
    ReleaseYear = db.Column(db.String(500),index=False,
        unique=False, nullable=True)
    created = db.Column(db.DateTime, index=False,
        unique=False, nullable=False
    )

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'rating': self.rating,
            'director': self.director,
            'actors': self.actors,
            'genre': self.genre,
            'runtime': self.runtime,
            'url': self.url,
            'type': self.type,
            'ReleaseYear': self.ReleaseYear,
            'created': self.created,
        }