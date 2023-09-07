class Vehicle:
    def __init__(self, reg_num, color):
        self.reg_num = reg_num
        self.color = color

    def __str__(self):
        return "Vehicle No: {}, Color: {}".format(self.reg_num, self.color)

class ParkingLot:
    def __init__(self, size):
        self.size = size
        self.slots = {key: None for key in range(1, size + 1)}
        print("Created a parking lot with {} slots".format(size))
    
    def get_nearest_parking_slot(self):
        for key, value in self.slots.items():
            if value is None:
                return key
        return "Parking is Full"

    def park_vehicle(self, vehicle):
        val = self.get_nearest_parking_slot()
        if isinstance(val, int):
            self.slots[val] = vehicle
            print("Allocated Slot {}".format(val))
        else:
            print("Slots Full. Please wait!")

    def leave_vehicle(self, slot):
        self.slots[slot] = None
        print("Slot number: {} is free to use ".format(slot))
    
    def status(self):
        for key, val in self.slots.items():
            if val is not None:
                print("Vehicle {} of color {} is parked at Slot:{}".format(val.reg_num, val.color, key))
            else:
                print("Slot {} is free to use".format(key))

class Utility:
    @staticmethod
    def get_reg_numbers_with_color(parking_lot, color):
        reg_numbers = [vehicle.reg_num for vehicle in parking_lot.slots.values() if vehicle and vehicle.color == color]
        print(reg_numbers)

    @staticmethod
    def get_slots_using_reg_num(parking_lot, reg_num):
        slots = [slot for slot, vehicle in parking_lot.slots.items() if vehicle and vehicle.reg_num == reg_num]
        print(slots)

    @staticmethod
    def get_slot_nums_using_color(parking_lot, color):
        slots = [slot for slot, vehicle in parking_lot.slots.items() if vehicle and vehicle.color == color]
        print(slots)

user_input = input("Enter Parking Lot Size ")
parking_lot = ParkingLot(int(user_input))

while True:
    command = input("Enter Your Command! ").split()
    if "park" in command:
        v = Vehicle(command[1], command[2])
        parking_lot.park_vehicle(v)
    elif "leave" in command:
        parking_lot.leave_vehicle(int(command[1]))
    elif command[0] == "status":
        parking_lot.status()
    elif command[0]=="registration_numbers_for_cars_with_colour":
        Utility.get_reg_numbers_with_color(parking_lot,command[1])
    elif command[0]=="slot_numbers_for_cars_with_colour":
        Utility.get_slot_nums_using_color(parking_lot,command[1])
    elif command[0]=="get_slot_nums_using_color":
        Utility.get_slots_using_reg_num(parking_lot,command[1])
    else:
        print("Exiting func")
        break