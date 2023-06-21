'''Functions
    1. In-Built Functions
    2. Module Functions
    3. User-Defined Functions
'''
'''
1. In-Built Functions
int()
str()
bool()
'''
'''
2. Module Functions

import math
print(dir(math))

'''
#pick anyone
from math import sqrt
print(sqrt(16))

#pick all
from math import *
print(sqrt(4))

'''
3. User-Defined Functions

def function_name(parameter):
    //do something


'''

def print_sum(first, second):
    print(first + second)

print_sum(1, 2)

def print_sum2(first, second = 5):
    print(first + second)

print_sum2(10)