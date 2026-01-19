class vehicle:
    vehicle_count=0
    def __init_subclass__(cls):
        vehicle.vehicle_count+=1
    def start(self):
        print("Vehicle is starting")

class BMW_Car(vehicle):
    def BMW(self):
        print("this a BMW car")

class SUV_Car(BMW_Car):
    def SUV(self):
        print("this a SUV car ")

obj=SUV_Car()
obj.start()
obj.BMW()
obj.SUV()
print(f"vehicle count : {obj.vehicle_count}")
