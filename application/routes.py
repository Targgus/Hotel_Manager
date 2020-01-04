from flask import Flask, render_template, request, make_response
from flask import current_app as app
from .models import Guest, db
import os

@app.route('/')
def index():
    return render_template('index.html', guests=Guest.query.all())

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        firstName = request.form['guestFirstName']
        lastName = request.form['guestLastName']
        roomNumber = request.form['roomNumber']

        if firstName and roomNumber:
            existing_user = Guest.query.filter(Guest.firstName == firstName).first()
        if roomNumber:
            existing_room = Guest.query.filter(Guest.roomNumber == roomNumber).first()
        if existing_user:
            return render_template('index.html', guests=Guest.query.all(), message='They are already checked in')
        if existing_room:
            return render_template('index.html', guests=Guest.query.all(), message='That room is currently booked')

        data = Guest(firstName=firstName, lastName=lastName, roomNumber=roomNumber)

        db.session.add(data)
        db.session.commit()
    return render_template('index.html', guests=Guest.query.all())

@app.route("/delete/<int:guestid>", methods=['GET', 'POST'])
def delete(guestid):
    Guest.query.filter_by(id=guestid).delete()
    db.session.commit()
    return render_template('index.html', guests=Guest.query.all())
