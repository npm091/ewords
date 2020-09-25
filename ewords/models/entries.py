from ewords import db
from datetime import datetime

# "id", "page", "number", "word", "remember", "Japanese", "example"
class Entry(db.Model):
    __tablename__ = 'ewords'
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.Integer)
    no = db.Column(db.Integer)
    english = db.Column(db.String(50))
    remember = db.Column(db.String(256))
    japanese = db.Column(db.String(256))
    example = db.Column(db.String(256))

    def __init__(self, id=None, page=None, no=None, english=None, remember=None, japanese=None, example=None):
        self.id = id
        self.page = page
        self.no = no
        self.english = english
        self.remember = remember
        self.japanese = japanese
        self.example = example

    def __repr__(self):
        return '<Entry page:{} no:{} english:{}>'.format(self.page, self.no, self.english)
