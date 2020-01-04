from flask import Flask, render_template, request, make_response
from flask import current_app as app
from .models import Guest, db
import os

# basic route
@app.route('/')
def index():
    # renders index.html and queries Guest table from sqlite and displays all guests
    return render_template('index.html', guests=Guest.query.all())

# route for form submission
@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        # grabs form data
        firstName = request.form['guestFirstName']
        lastName = request.form['guestLastName']
        roomNumber = request.form['roomNumber']

        # checks if firstname exists
        if firstName:
            # creates existing_user variable based on information within the database
            existing_user = Guest.query.filter(Guest.firstName == firstName).first()
        # checks is roomnumber exists
        if roomNumber:
            # creates existing_room variable based on information within the database
            existing_room = Guest.query.filter(Guest.roomNumber == roomNumber).first()
        # if existing user and existing room exist, send message back to index and do not allow database submission
        if existing_user:
            return render_template('index.html', guests=Guest.query.all(), message='They are already checked in')
        if existing_room:
            return render_template('index.html', guests=Guest.query.all(), message='That room is currently booked')

        # build variable that holds Guest object filled in with form data
        data = Guest(firstName=firstName, lastName=lastName, roomNumber=roomNumber)

        # add data variable to database
        db.session.add(data)
        # commit data
        db.session.commit()
    # render index will all guests from database
    return render_template('index.html', guests=Guest.query.all())

@app.route("/delete/<int:guestid>", methods=['GET', 'POST'])
def delete(guestid):
    Guest.query.filter_by(id=guestid).delete()
    db.session.commit()
    return render_template('index.html', guests=Guest.query.all())
