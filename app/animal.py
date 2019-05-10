from app import db

class Animal(db.Model):

    # __tablename__ = "animal"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    breed = db.Column(db.String(30), nullable=False)
    picture_url = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(80), nullable=True)
    activity = db.Column(db.String(30), nullable=True)
    donation = db.relationship("Donation", back_populates="animal")
    intention = db.relationship("Intention", back_populates="animal")

    def __init__(self, name, breed, picture_url, gender, age, availability, activity="Playing toys", id=None):
        self.id = id
        self.breed = breed
        self.name = name
        self.picture_url = picture_url
        self.gender = gender
        self.age = age
        self.availability = availability
        self.activity = activity

    def __repr__(self):
        return '<Animal %r>' % (self.name)

    def __eq__(self, other):
        return int(self.id) == int(other.id)
