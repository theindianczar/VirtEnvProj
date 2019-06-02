#tuple
numbers =(1,2,3,4,5,6)
letters=('a','b','c','d')
m=('a',23,10.5)

#nested tuple
two_dim = ((2,3),(5,3),(7,2))

print(m[2])
print(two_dim[1][1])

#pack and unpack tuples
packing_tuple = 2,5,'Space'
print(packing_tuple)

a,b,c = packing_tuple

print(a)
print(b)
print(c)
print(packing_tuple)


numbers =(8,9,2,3,4,5,6)
letters=('a','b','c','d')


#slicing with tuples
print(numbers[2:5])
print(numbers[1:])

even_nums=numbers[::2]
odd_nums=numbers[1::2]
print('even nums',even_nums)
print('odd nums',odd_nums)


# iterating with tuples

for letter in letters+numbers:
    print(letter)

# function with tuples

def area_and_circumference_of_circle(radius):
    import math
    return(math.pi*radius**2,2*math.pi*radius)

print(area_and_circumference_of_circle(9))