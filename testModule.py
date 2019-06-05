#import myModule
from myModule import *
r=float(input('please enter radius'))

print('circumference of circle with radius',r, 'is',circumference(r))
print('area of circle with radius',r, 'is',area(r))

#import externalModule
from externalModule import *

print(area(12))
