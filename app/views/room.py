__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,json,request,
                   abort, flash)
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
from app.forms import room as room_details
from flask_restful import Resource, Api,reqparse
import fileinput
from requests import put, get
# Serializer for generating random tokens
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Create a user blueprint
roombp = Blueprint('roombp', __name__, url_prefix='/room')
api = Api(app)


@roombp.route('/addRoom', methods=['GET', 'POST'])
@login_required
def addRoom():
    form = room_details.Rooms()
    if form.validate_on_submit():
        room = models.Room(
            number=form.number.data,
            type=form.type.data,
            availability=True,

        )
        # Insert the room in the database
        db.session.add(room)
        db.session.commit()

        flash('added room details sucessfully.', 'positive')
        return redirect(url_for('index'))
    return render_template('room/details.html', form=form, title='Room Details')


@roombp.route('/showRooms', methods=['GET', 'POST'])
@login_required
def showRooms():
    rooms = models.Room.query.all()
    return render_template('room/showDetails.html', title='Room', rooms=rooms)


customers={}
class getCustomerId(Resource):
    def get(self,customerId):
        #print(CustomerId)
        return{'data':'recived'}
    # def put(customerId):
    #       customers[customerId] = request.form['data']
    #       return {customerId:customers[customerId]}


api.add_resource(getCustomerId,'/sendCustomer')