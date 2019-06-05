from collections import OrderedDict

a=OrderedDict(name='Tiger',role='animal',home='jungle')
b={}

dictionary_functions=dir(b)
OrderedDict_functions=dir(a)
'''
print(dictionary_functions)
for f in dictionary_functions:
    print(f.__doc__)

for f in OrderedDict_functions:
    if f not in dictionary_functions:
        print(f)
'''

a=OrderedDict(name='Tiger',role='animal',home='jungle')
b=OrderedDict(name='Tiger',home='jungle',role='animal')
print(a==b)

c={'name':'Tiger','role':'animal','home':'jungle'}
print(a==c)