class Cat:
    def __init__(self,mass,lifespan,speed):
        self.lifespan_in_years=lifespan
        self.mass_in_kg=mass
        self.speed_in_kph=speed

    def vocalize(self):
        print('meeeow')

class Leopard(Cat):
    print('wwwww')

tomy=Cat(5,17,16)

leo=Leopard(90,37,120)
leo.vocalize()
print(leo.__dict__)