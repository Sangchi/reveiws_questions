'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]


'''


def sum_target(list,target):

    n=len(list)
    new_list=[]
    for i in range(n):
        for j in range(i+1,n):
            if list[i]+list[j]==target:
                new_list.append(i)
                new_list.append(j)

    return new_list

list_item=[3,2,4,3]
user_target=6

print(sum_target(list_item,user_target))
