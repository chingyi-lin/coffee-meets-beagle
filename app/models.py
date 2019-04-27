from app import app, login_manager, user, db
from flask_login import UserMixin, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .user import User


# --- Database API ---

def addToDatabase(newObject):
    db.session.add(newObject)
    db.session.commit()
    return 

def getUserByUsername(query):
    return User.query.filter_by(username=query).first()

# --- Login/Sign Up Helper Methods ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def isUsernameUsed(username):
    user = User.query.filter_by(username=username).first()
    return False if user is None else True
    
def isEmailUsed(email):
    user = User.query.filter_by(email=email).first()
    return False if user is None else True
    
def validateLogin(username, password):
    comparedUser = getUserByUsername(username)
    if comparedUser is None or not check_password_hash(comparedUser.password_hash, password):
        return False
    login_user(comparedUser)
    return True