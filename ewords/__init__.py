from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ewords.config')

db = SQLAlchemy(app)

from ewords.views import views

