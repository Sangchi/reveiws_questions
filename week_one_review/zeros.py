'''
4.Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of the non-zero elements.
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]
Input: [0,1,0,3,12]
Output: [1, 3, 12, 0, 0]

Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

'''

def zeros_end(list):

    num=0
    result=[]
    for i in list:
        if i==num:
            list.remove(i)
            list.append(i)

    return list

list_item=[0,1,0,3,12]

print(zeros_end(list_item))

    
