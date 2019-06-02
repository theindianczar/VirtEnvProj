sentence = 'have a nice day'
numbers = [1,2,3,4,5,6,7,8]
#tuple ()
letters= ('a','b','c','d')

for c in sentence:
    print (c)

for n in numbers:
    print(n)

for letter in letters:
    print(letter.center(3,'#'))

num =int(input("provide a number here"))
print('here is a times table for',num)
for i in range(1,11):
    print(i*num)