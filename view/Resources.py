"""
information of flask-restfull and JWT
https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb
http://polyglot.ninja/jwt-authentication-python-flask/
"""
# Library for consult API coindesk.com
import requests
# Library convert data in json
from flask import jsonify
# Flask restful library
from flask_restful import Resource, reqparse
# Library equivalent AND SQL
from sqlalchemy import and_
# Models
from model.models import Session, BtcHistory


class Price(Resource):
    def get(self):
        # Obtain request from price in peso ARS
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/ARS.json')
        # Convert request in JSON
        jsonrequest = r.json()

        time = jsonrequest['time']['updated']
        arsprice = jsonrequest['bpi']['ARS']['rate_float']
        usdprice = jsonrequest['bpi']['USD']['rate_float']
        arcode = jsonrequest['bpi']['ARS']['code']
        uscode = jsonrequest['bpi']['USD']['code']
        # Save data in dictionary
        context = {
            'tiempo': time,
            'arsprice': arsprice,
            'arcode': arcode,
            'usdprice': usdprice,
            'uscode': uscode
        }
        # Return data in JSON
        return jsonify(context)


class AllData(Resource):
    def get(self):
        # Open session in database
        session = Session()
        # Get all BTC history using btc model
        btcHistory = session.query(BtcHistory).all()
        # Close session in database
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in btcHistory]
        })


class Date(Resource):
    def get(self):
        # Object parser and create argument
        parser = reqparse.RequestParser()
        parser.add_argument('date', help='This field cannot be blank', required=True)
        # Open session in database
        session = Session()
        # Obtain date variable argument in GET method
        date_ = parser.parse_args()
        # Get date from Btc History model with target
        btcHistory = session.query(BtcHistory).filter(BtcHistory.date == date_['date'])
        # Close session in database
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in btcHistory]
        })


class DateRange(Resource):
    def get(self):
        # Object parser and create argument
        parser = reqparse.RequestParser()
        parser.add_argument('startdate', help='This field cannot be blank', required=True)
        parser.add_argument('enddate', help='This field cannot be blank', required=True)
        # Open session in database
        session = Session()
        data = parser.parse_args()
        # Obtain startdate and enddate from GET method
        startdate = data['startdate']
        enddate = data['enddate']
        # Consult database and utilice AND from SQL in filter with and _ library
        btcHistory = session.query(BtcHistory).filter(and_(
            BtcHistory.date >= startdate,
            BtcHistory.date <= enddate
        )).all()
        # Close session in database
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in btcHistory]
        })


class RangeVariation(Resource):
    def get(self):
        # Object parser and create argument
        parser = reqparse.RequestParser()
        parser.add_argument('startvar', help='This field cannot be blank', required=True)
        parser.add_argument('endvar', help='This field cannot be blank', required=True)
        session = Session()
        # Obtain startvar and endvar from GET method
        data = parser.parse_args()
        startvar = data['startvar']
        endvar = data['endvar']
        # Consult database and utilice AND from SQL in filter with and _ library
        btcHistory = session.query(BtcHistory).filter(and_(
            BtcHistory.var >= startvar,
            BtcHistory.var <= endvar
        )).all()
        # Close session in database
        session.close()
        # Return all data in JSON
        return jsonify({
            'data': [result.serialized for result in btcHistory]
        })
