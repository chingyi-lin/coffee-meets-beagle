from app import db

class Animals(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    picture_url = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80))
    age = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(80))

    def __init__(self, name, picture_url, gender, age, availability, id=None):
        self.id = id
        self.name = name
        self.picture_url = picture_url
        self.gender = gender
        self.age = age
        self.availability = availability
