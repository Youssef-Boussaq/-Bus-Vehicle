class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def show(self):
        print("Vehicle Name: {} Speed: {} Mileage: {}".format(self.name , self.max_speed , self.mileage))
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
      super().__init__( name, max_speed, mileage)
df = Bus("School Volvo", 180 , 12)
df.show()