import uuid
import bisect

class ParkingArea:
    def __init__(self, address, total_slots):
        self.__id = uuid.uuid1()  # unique id for each parking space
        self.__location = address    # 
        self.__total_slots = total_slots

class ParkingSlot(ParkingArea):
    def __init__(self, address=None, total_slots=0):
        self.available_slots = [x for x in range(1,int(total_slots)+1)]
        super().__init__(address, total_slots)

    def is_free(self):
        return True if self.available_slots else False

    def get_closest_available_slot(self):
        return self.available_slots and self.available_slots.pop(0) or -1
        #self.available_slots and self.available_slots.pop(0)

    def remove_vehicle(self, slot):
        slot = int(slot)
        return True if slot not in self.available_slots and bisect.insort(self.available_slots, slot) else False
