import time


num=int(input("enter a number"))
tic= time.clock()

prime=True

for i in range(2,num):
    if(num%i==0):
        prime=False
        break
toc= time.clock()

if prime==True:
    print(num,'is prime')
else:
    print(num,'is not prime')


print('time taken ',toc-tic)