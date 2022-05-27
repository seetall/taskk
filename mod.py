"""def add(a,b):
    print(a+b)
if __name__=="__main__":
    add(2,3)"""
'''
a=2.45678
print(round(a,2))'''

#fabs: +ve value (-4.5) output 4.5
#pow(4,2)
'''
import math
a=2.5983
print(math.floor(a))

import math
a=4.67
print(math.ceil(a))

import math
a=-4.98
print(math.fabs(a))

import math
a=5
print(math.factorial(a))

import math
a=16
print(math.sqrt(a))

import math
a=4
b=2
print(math.pow(a,b))'''
''''
import random
list1=[1,2,3,4,5,6]
print(random.choice(list1))'''
'''
import random
r1=random.randint(5,15)
print("Random number between 5 and 15 is % s" % (r1))
r2=random.randint(-10,-2)
print("Random number between -10 and -2 % d" % (r2))'''
'''
import random
sample_list=[1,2,3,4,5]
print("original list: ")
print(sample_list)
random.shuffle(sample_list)
print(sample_list)'''
'''
import random
for i in range(50):
    print(random.randint(20,50))'''
'''
import random
list=[]
n=int(input("Enter a number: "))
for i in range(n):
    list.append(random.randint(1,20))
    print(list)'''
'''
import datetime
x=datetime.datetime.now()
print(x)'''

import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("A%","a%","%W","%d","%b","%B","%m","%y","%Y"))

