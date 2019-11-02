from . import db

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key = True, unique=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    roomNumber = db.Column(db.Integer)

    def __repr__(self):
        return '<Guest {}>'.format(self.firstName)