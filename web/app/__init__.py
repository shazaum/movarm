from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from yaml import YAMLError,safe_load

try:
    dataConfig = open('app/configs/data.yaml', 'r')
    config = safe_load(dataConfig)
except YAMLError as exc:
    print("Error in configuration file:", exc)

username = config['db']['username']
password = config['db']['password']
database = config['db']['database']
host = config['db']['host']
port = config['db']['port']

app = Flask(__name__)
POSTGRES = {
    'user': username,
    'pw': password,
    'db': database,
    'host': host,
    'port': port,
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.controllers import main
