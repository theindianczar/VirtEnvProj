a='helllo'
b='everyone'

message=a+' '+b

print(message)

message=message+'!'
message+= '!'

long_message = message*5
print(message)
print(long_message)

color =input('enter the color value')
r=color[0:2]
g=color[2:4]
b=color[4:]
print(r,g,b)

r=int(r,16)
g=int(g,16)
b=int(b,16)

print(r,g,b)


# using format to insert variable inside string
fruit="bananas"
color="brownish"
print("I love {} which are of {} color".format(fruit,color))