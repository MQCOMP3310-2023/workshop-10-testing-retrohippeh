from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password, password_plaintext)
    def set_password(self, password_plaintext: str):
        self.password = generate_password_hash(password_plaintext)