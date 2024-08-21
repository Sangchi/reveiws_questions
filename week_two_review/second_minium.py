'''
Given a list of integers, write a Python script to find the second min without using any in-built sorting or max/min functions.
Input: [2, 11, 15, 66, 20]
Output: Second largest: 20

'''
# def second_minimum(array):

#     n=len(array)
#     for i in range(n):
#         for j in range(n-i-1):
#             if array[j]>array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp

#     return array[1],array[0]

# array_list=[2, 12, 11, 66, 20]
# print(second_minimum(array_list))

# def second_minium(array):

#     list=[]
#     second_min=array[1]
#     min=array[0]
#     for i in range(len(array)):
#         if array[i]<min:
#             second_min=min
#             min=array[i]

#         if array[i]<second_min and array[i]>min:
#             second_min=array[i]

#     return second_min,min

# array_list=[2, 11,9, 15, 66, 20]
# print(second_minium(array_list))

# def second_max_element(array):
    
#     max=array[0]
#     second_max=array[0]
#     n=len(array)

#     for i in range(n):
#         if array[i]>max:
#             second_max=max
#             max=array[i]


#         if array[i]>second_max and array[i]<max:
#             second_max=array[i]

#     return second_max,max

# array_list=[1,2,3,5,6,7,8,12,10]

# print(second_max_element(array_list))

# def third_max_element(array):

#     n=len(array)
#     max=array[0]
#     second_max=array[0]
#     third_max=array[0]
#     for i in range(n):

#         if array[i] >max:
#             third_max=second_max
#             second_max=max
#             max=array[i]

#         if array[i]>third_max and array[i]<second_max and array[i]<max:
#             third_max=array[i]

#     return third_max

# array_list=[1,2,3,4,5,6,7,8,9,10]

# print(third_max_element(array_list))


#print distinct sorted list

def distinct_list(array):

    list=[]
    n=len(array)
    for i in range(n):
        if array[i] not in list:
            list.append(array[i])

    return list

array_list=[1,2,2,3,4,5,4,5,7,6]

list1=distinct_list(array_list)

n=len(list1)
for i in range(n):
    for j in range(n-i-1):
        if list1[j]>list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp

print(list1)
