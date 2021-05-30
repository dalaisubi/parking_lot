from abc import ABC

class Vehicle:
    def __init__(self, registration_number, ticket, vehicletype=None):
        self.registration_number = registration_number
        self.__type = vehicletype
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket


class Car(Vehicle):
    def __init__(self, registration_number, ticket, vehicletype="Car"):
        super().__init__(registration_number, ticket, vehicletype=vehicletype)