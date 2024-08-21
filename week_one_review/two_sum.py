# def two_sum(array,target):
    
#     n=len(array)
#     for i in range(n):
#         for j in range(i+1,n):
#             if array[i]+ array[j]==target:
#                 return True
#     return f"two sum is not fount"
# array_item=[2,3,4,5,6]
# user_target=int(input("enter the target:"))

# print(two_sum(array_item,user_target))

def two_sum(array,target):

    array.sort()
    left=0
    right=len(array)-1
    while left <right:
        current_sum=array[left]+array[right]

        if current_sum==target:
            return True
        elif current_sum <target:
            left +=1
        else:
            right -=1

    return False
array_item=[2,4,5,1,6,8,7,10,9]
user_target=int(input("enter user input:"))

print(two_sum(array_item,user_target))

