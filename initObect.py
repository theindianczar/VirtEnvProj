class Car:

    def __init__(self, make, model, year, weight,max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.speed=0
        self.max_speed=max_speed

    def accelerate(self,add_speed=5):
        self.speed+=add_speed
        if(self.speed>self.max_speed):
            self.speed=self.max_speed

# initialize car
my_car = Car('mazda', '6', 2010, 1200,220)
dream_car = Car('test', '12', 2019, 1600,180)

for i in range(0,10):
    my_car.accelerate(20)
    my_car.accelerate(25)
    dream_car.__dict__

# print obect attr
print(my_car.__dict__)
print(dream_car.__dict__)
print('dream car is', dream_car.make)

# create new attr for speed and max speed
