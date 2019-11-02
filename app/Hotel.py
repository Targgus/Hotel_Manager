import numpy as np
from .Guest import Guest

class Hotel():
    occupiedRooms = 0
    
    def __init__(self, numberOfRooms, roomArray):
        self.numberOfRooms = numberOfRooms
        self.roomArray = roomArray
    
    def updateOccupancy(self):
        self.occupiedRooms = 0
        for key, guest in self.roomArray.items():
            if guest:
                self.occupiedRooms += 1

    def returnStats(self):
        return "There are {} rooms at this hotel but {} are occupied.".format(self.numberOfRooms, self.occupiedRooms)

    def setOccupant(self, roomNum, guest):
        self.roomArray[roomNum] = guest 
        self.updateOccupancy()

    def removeOccupant(self, roomNum, guest):
        self.roomArray[roomNum] = None
        self.updateOccupancy()
        

    def getOccupants(self):
        for key, guest in self.roomArray.items():
            if guest:
                return guest.getName()

    def getOccupiedRooms(self):
        for key, val in self.roomArray.items():
            if val:
                return key

    def getAllRooms(self):
        for val, key in self.roomArray.items():
            print(key[0])

    def checkVacancy(self):
        if self.occupiedRooms >= self.numberOfRooms:
            return False
        else:
            return True 
    


