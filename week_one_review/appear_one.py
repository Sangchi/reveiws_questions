'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
Input: nums = [4,1,2,1,2]
Output: 4

'''

def find_single_number(nums):
    
    num_list = []
    for num in nums:
        if num in num_list:
            num_list.remove(num)
        else:
            num_list.append(num)
    
    
    return num_list

print(find_single_number([2, 2, 1]))
print(find_single_number([4, 1, 2, 1, 2]))

