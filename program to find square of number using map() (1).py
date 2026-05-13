#program to find square of number using map()
from functools import reduce

num=[1,2,3,4,5]
squares=list(map(lambda x:x**2,num))
print("original list:",num)
print("squares:",squares)