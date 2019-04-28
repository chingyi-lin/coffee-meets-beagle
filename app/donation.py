from app import db

class Donation(db.Model):

    # __tablename__ = "donation"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="donation")
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'))
    animal = db.relationship("Animal", back_populates="donation")
    

    def __init__(self, amount, date, user_id, animal_id, id=None):
        self.id = id
        self.amount = amount
        self.date = db.func.now()
        self.user_id = user_id
        self.animal_id = animal_id

    def __repr__(self):
        return '<Donation %r>' % (self.id)

    def __eq__(self, other):
        return int(self.id) == int(other.id)
