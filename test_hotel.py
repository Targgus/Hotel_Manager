import unittest
from Hotel import Hotel
import numpy as np

class TestHotel(unittest.TestCase):

    
    roomArray = np.arange(1, 4, 1)
    hotel = Hotel(3, 0, 0, roomArray)

    def test_returnRooms(self, hotel):
        testArray = np.arange(1, 4, 1)
        np.testing.assert_array_equal(testArray, hotel.returnRooms())

    # def test_returnStats(self):