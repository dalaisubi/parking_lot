from parking_lot import ParkingSlot
import vehicle
import uuid, enum
import datetime

class ParkingTicketStatus(enum.Enum):
    ACTIVE, END = 1, 2

class ParkingTicket:
    def __init__(self, status=ParkingTicketStatus.ACTIVE):
        self.__ticket = uuid.uuid1()
        self.issued_at = datetime.datetime.now()
        self.end_at = None
        self.status = status

    def generate_ticket(self):
        return self.__ticket

    def update_ticket(self, status, end_at):
        self.status = status
        self.end_at = end_at


class ParkingService(ParkingSlot):
    def __init__(self):
        self.list_of_parkings_details = []

    def create_parking_lot(self, total_slot):
        address = "Default address"
        super().__init__(address, total_slot)


    def park(self, registration_number, age_of_driver):
        if self.is_free:
            parking_details = {}
            parking_details['slot_id'] = self.get_closest_available_slot()
            parking_details['vehicle_obj'] = vehicle.Car(registration_number, ParkingTicket().generate_ticket() ,ParkingTicketStatus.ACTIVE)
            parking_details['age_of_driver'] = age_of_driver

            self.list_of_parkings_details.append(parking_details)

            print(f'Car with vehicle registration number {registration_number} has been parked at slot number {parking_details["slot_id"]}')

            return parking_details['slot_id']
        else:
            print("Parking lot is full")
            return -1

    def leave(self, slot_id):
        registration_number = ""
        age = 0
        for ind, x in enumerate(self.list_of_parkings_details):
            if x.get('slot_id') == slot_id:
                registration_number = x.get("vehicle_obj").registration_number
                age = x.get('age_of_driver')
                self.list_of_parkings_details.pop(ind)
        print(f'Slot number {slot_id} vacated, the car with vehicle registration number {registration_number} left the space, the driver of the car was of age {age}')
        return self.remove_vehicle(slot_id)

    def slot_numbers_for_driver_of_age(self, age_of_driver):
        slot_ids = [str(x.get('slot_id')) for x in self.list_of_parkings_details if x['age_of_driver'] == age_of_driver]
        if slot_ids:
            print(",".join(slot_ids))
        else:
            print("No parked car matches the query")
        return slot_ids

    def slot_number_for_car_with_number(self, registration):
        #embed()
        slot_ids = [str(x.get('slot_id')) for x in self.list_of_parkings_details if x.get('vehicle_obj').registration_number == registration]
        if slot_ids:
            print(",".join(slot_ids))
        else:
            print("No parked car matches the query")
        return slot_ids

    def vehicle_registration_number_for_driver_of_age(self, age_of_driver):
        reg_number = [x.get("vehicle_obj").registration_number for x in self.list_of_parkings_details if x['age_of_driver'] == age_of_driver]
        if reg_number:
            print(",".join(reg_number))
        else:
            print("No parked car matches the query")
        return reg_number 



