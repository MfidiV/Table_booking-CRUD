from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Booking

main = Blueprint('main', __name__)
"""
 Displays all bookings on the homepage by:
   - Querying all booking records from the database.
   - Converting each booking object to a dictionary.
   - Passing the list of dictionaries to the template for rendering.
"""
@main.route('/', methods=['GET'])
def index():
   # Query all booking records from the database
   bookings = Booking.query.all()

   # Convert SQLAlchemy Booking objects into dictionaries for easier template rendering
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

   # Render the 'bookings.html' template and pass the bookings data to it
   return render_template('bookings.html', bookings=bookings_data)
