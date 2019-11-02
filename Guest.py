class Guest():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def setName(self, firstName, lastName):
        self.first = firstName
        self.last = lastName

    def getName(self):
        return self.first + " " + self.last