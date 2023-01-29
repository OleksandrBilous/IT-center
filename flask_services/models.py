from flask_login import UserMixin

from flask_services import db, manager, migrate, cb


class User (db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    
@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)