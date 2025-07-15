from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import db, Booking
from datetime import date

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
   current_date = date.today().isoformat()

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
   return render_template('bookings.html', bookings=bookings_data, current_date=current_date)


#Handles the form submission to add a new booking.
@main.route('/add', methods=['POST'])
def add_booking():
    name = request.form.get('name')
    table_number = request.form.get('table_number')
    date = request.form.get('date')
    time = request.form.get('time')

    if not (name and table_number and date and time):
        return redirect(url_for('main.index'))

    new_booking = Booking(name=name, table_number=int(table_number), date=date, time=time)
    db.session.add(new_booking)
    db.session.commit()

    return redirect(url_for('main.index'))

# Deletes a specific booking based on its unique ID.
@main.route('/delete/<int:booking_id>', methods=['GET'])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.delete(booking)
    db.session.commit()
    return redirect(url_for('main.index'))


"""Update the booking fields with form data 
Save changes to the database and return a success response with 
updated booking info"""
@main.route('/edit/<int:booking_id>', methods=['POST'])
def edit_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    booking.name = request.form.get('name')
    booking.table_number = int(request.form.get('table_number'))
    booking.date = request.form.get('date')
    booking.time = request.form.get('time')

    db.session.commit()

    return jsonify({
        'success': True,
        'booking': {
            'id': booking.id,
            'name': booking.name,
            'table_number': booking.table_number,
            'date': booking.date,
            'time': booking.time
        }
    })