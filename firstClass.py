#create a car Class

class Car():
    pass

#create a car obect
honda=Car()
mazda=Car()

# add attributes to the car obect
honda.model = "CRW"
honda.weight = 1200

#print attributes
print('Honda model is ', honda.model)
print('Honda weight is ', honda.weight)

print(honda.__dict__)
print(mazda.__dict__)
