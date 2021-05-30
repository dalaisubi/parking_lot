from run_script import ParkingService
import json


FUNCTION_LIST = [
    "create_parking_lot",
    "park",
    "slot_numbers_for_driver_of_age",
    "leave",
    "slot_number_for_car_with_number",
    "vehicle_registration_number_for_driver_of_age",
]


def read_files():
    bool_ = False
    with open("input.txt", "r") as f:
        input_ = f.readlines()

    bool_ = input_validity_check(input_)
    if bool_:
        parking_obj = ParkingService()

        for i in input_:
            #if 'driver_age' in i:
            func, *args = i.replace('driver_age', '').split()
            tmp_ = func.lower()
            if tmp_ in FUNCTION_LIST:
                print(tmp_)
                eval("parking_obj." +tmp_)(*args)

def input_validity_check(input_):
    if 'create_parking_lot' in input_[0].lower():
        return True
    print("***********************************************")
    print("Opps! something went wrong with the input file.")
    print("***********************************************")
    return False

read_files()