#create set
a={1,2,3}
b={3,4,5}

#print elements
print(a)

#iterate through sets
for item in a:
    print(item)

#add elements
a.add(4)
print(a)
a.update(b)
print(a)

#remove items
a.remove(5)
a.discard(4)
print(a.pop())
print(a)

a={1,2,3}
b={3,4,5}
print(a.symmetric_difference(b))