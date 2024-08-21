'''
Given a list of integers, write a Python script to find the second largest without using any in-built sorting or max/min functions.
Input: [2, 11, 15, 66, 20]
Output: Second largest: 20

'''
def second_max(array):

    max=array[0]
    second_max_element=array[0]
    for i in range(1,len(array)):

        if array[i]>max:
            second_max_element=max
            max=array[i]

        if array[i]>second_max_element and array[i] <max:
            second_max_element=array[i]

    return second_max_element

array_list=[2, 11, 15, 66, 20,45]

print(second_max(array_list))
            
