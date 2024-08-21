# def second_maximum(array):
    
#     n=len(array)
#     temp=0
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if array[j]>array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp

#     return array
# array_item=[2,3,4,1,5,6,9,8,7]
# print(second_maximum(array_item))
# n=len(array_item)
# max=len(array_item)
# second_max=0
# for i in range(n):
#     if array_item[i]<max:
#         second_max=array_item[i]

# print(second_max)

# '''
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 8


# '''

# def happy_number(n):
#     def get_number(number):
#         return sum(int(digit)**2 for digit in str(number))
    
#     sen=set()
#     while n!=1 and n not in sen:
#         sen.add(n)
#         n=get_number(n)

#     return n==1

# number=21
# print(happy_number(number))
        

        
