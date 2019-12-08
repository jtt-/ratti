# db määritelty __init__.py tiedostossa
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

    
class User(db.Document, UserMixin):

    meta = {'collection':'user'}
    email = db.StringField(max_length=64)
    password = db.StringField()
    username = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()
