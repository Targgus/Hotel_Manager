from app.Hotel import Hotel
from app.Guest import Guest
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./app/templates')

rooms = 5
roomArray = dict.fromkeys(np.arange(1, rooms+1, 1))
hotel = Hotel(rooms, roomArray)


@app.route('/')
def index():
    vacancy = hotel.checkVacancy()
    return render_template('index.html', hotel=hotel, vacant = vacancy, occupiedRoomCount = hotel.occupiedRooms)

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        guest = Guest(request.form['guestFirstName'], request.form['guestLastName'])
        room = request.form['roomNumber']

        hotel.setOccupant(int(room), guest)
        # print(hotel.roomArray.items())
        vacancy = hotel.checkVacancy()
        print(vacancy)
    return render_template('index.html', hotel = hotel, occupiedRoomCount = hotel.occupiedRooms, vacant = vacancy)

@app.route("/remove", methods=['POST'])
def remove():
    if request.method == "POST":
        guest = Guest(request.form['guestFirstNameCO'], request.form['guestLastNameCO'])
        room = request.form['roomNumberCO']

        hotel.removeOccupant(int(room), guest)
        vacancy = hotel.checkVacancy()
        print(vacancy)
    return render_template('index.html', hotel = hotel, occupiedRoomCount = hotel.occupiedRooms, vacant = vacancy)



if __name__ == '__main__':
    app.debug = True
    app.run()

