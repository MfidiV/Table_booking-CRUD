from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Booking

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
   bookings = Booking.query.all()

   # Convert SQLAlchemy objects to dictionaries
   bookings_data = [
       {
           'id': b.id,
           'name': b.name,
           'table_number': b.table_number,
           'date': b.date,
           'time': b.time
       }
       for b in bookings
   ]

   return render_template('bookings.html', bookings=bookings_data)