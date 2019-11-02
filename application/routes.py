from flask import Flask, render_template, request, make_response
from flask import current_app as app
from .models import Guest, db
import os

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        firstName = request.form['guestFirstName']
        lastName = request.form['guestLastName']
        roomNumber = request.form['roomNumber']

        if firstName and roomNumber:
            existing_user = Guest.query.filter(Guest.firstName == firstName or Guest.roomNumber == roomNumber).first()
        if existing_user:
            return make_response(f'{firstName} ({roomNumber}) alreday checked in!')

        data = Guest(firstName=firstName, lastName=lastName, roomNumber=roomNumber)

        db.session.add(data)
        db.session.commit()
    return render_template('index.html', guests=Guest.query.all())
