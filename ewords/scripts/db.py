from flask_script import Command
from ewords import db
from ewords.models.entries import Entry
import csv


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()

class InsertTable(Command):
    "insert into table"
    def run(self):
        csvrfile = open('data/ewords.csv')
        csv_reader = csv.reader(csvrfile, delimiter=',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            entry = Entry(
                id=row[0],
                page=row[1],
                no=row[2],
                english=row[3],
                remember=row[4],
                japanese=row[5],
                example=row[6]
            )
            db.session.add(entry)
        db.session.commit()
