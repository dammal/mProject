__author__ = 'Raditha'
from flask import (Blueprint, render_template, redirect, url_for,request,
                   abort, flash)
from flask_restful import Resource, Api
from flask.ext.login import login_user, logout_user, login_required
from itsdangerous import URLSafeTimedSerializer
from app import app, models, db
ts = URLSafeTimedSerializer(app.config['SECRET_KEY'])
api = Api(app)
customers={}
# class getCustomerId(Resource):
#     def get(data,customerId):
#         return{'data':'recived'}
#     def put( customerId):
#         customers[customerId] = request.form['data']
#         return {customerId: customers[customers]}
#
# api.add_resource(getCustomerId,'/sendCustomer')