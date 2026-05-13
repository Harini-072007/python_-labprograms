#program to filter even numbers using filter()
num=[1,2,3,4,5]
even_num=list(filter(lambda x:x%2==0,num))
print("Even number is:",even_num)