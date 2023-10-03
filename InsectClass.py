import random

class Insect:
    def __init__(self,w,l,n):
        self.wings=w
        self.legs=l
        self.flight_length=0
        self.name=n

    def fly(self):
        self.flight_length=random.randint(0,10)

    def get_flight_length(self):
        return self.flight_length
