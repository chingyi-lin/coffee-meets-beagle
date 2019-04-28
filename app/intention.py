from app import db

class Intention(db.Model):

    # __tablename__ = "intention"

    id = db.Column(db.Integer, primary_key=True)
    acitivit_type = db.Column(db.String(15), nullable=False)
    timeslots = db.Column(db.DateTime, nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="intention")
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship("Animal", back_populates="intention")
    

    def __init__(self, acitivit_type, timeslots, user_id, animal_id, id=None):
        self.id = id
        self.acitivit_type = acitivit_type
        self.timeslots = timeslots
        self.date = db.func.now()
        self.user_id = user_id
        self.animal_id = animal_id

    def __repr__(self):
        return '<Intention %r>' % (self.id)

    def __eq__(self, other):
        return int(self.id) == int(other.id)
