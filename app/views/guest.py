__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import room as room_details
from flask_restful import Resource, Api
from requests import put, get
from app.forms import guest as guest_details
# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
guestbp = Blueprint('guestbp', __name__, url_prefix='/guest')
api = Api(app)


@guestbp.route('/addGuest', methods=['GET', 'POST'])
@login_required
def addGuest():
    form = guest_details.Guests()
    if form.validate_on_submit():
        guest = models.Guest(
            number=form.number.data,
            type=form.type.data,
            availability=True,

        )
        # Insert the room in the database
        db.session.add(guest)
        db.session.commit()

        flash('added guest details sucessfully.', 'positive')
        return redirect(url_for('index'))
    return render_template('guest/details.html', form=form, title='Guest Details')


@guestbp.route('/showRooms', methods=['GET', 'POST'])
@login_required
def showGuests():
    guests = models.Guest.query.all()
    return render_template('guest/showDetails.html', title='Room', guests=guests)
