#program to find the sum of list elements using reduce()
num=[1,2,3,4,5,6]
sum_of_numbers= reduce(lambda x,y:x+y,num)
print("sum:",sum_of_numbers)