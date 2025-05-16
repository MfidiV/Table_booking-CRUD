from .db import db

""" 
 Booking Model
 Represents a table booking in the system. Each record stores the name of the
 customer, the table number, and the booking date and time.
"""
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        # String representation used for debugging and logging
        return f"<Booking {self.name} - Table {self.table_number}>"