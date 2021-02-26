"""
Flask app starting routines
"""
import os
import sqlite3
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


if not os.path.exists(app.config["DATABASE_NAME"]):
    conn = sqlite3.connect(app.config["DATABASE_NAME"])
    cur = conn.cursor()
    create_query = "CREATE TABLE REVIEW (ID INTEGER PRIMARY KEY AUTOINCREMENT, REVIEW varchar(255) NOT NULL, PREDICTION int, feedback int)"
    cur.execute(create_query)
    conn.commit()

db = SQLAlchemy(app)

from app import routes  # noqa