from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import couchdb
import redis


app = Flask(__name__)
app.secret_key = 'my secret key123321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@postgres:5432/itservice'
couch = couchdb.Server('http://alex:12345@couch:5984/')
redis_conection = redis.Redis(host='redis', port=6379, db=0)

cb = couch['order']

db =SQLAlchemy(app)
migrate = Migrate(app, db)
manager = LoginManager(app)


from flask_services import routes

