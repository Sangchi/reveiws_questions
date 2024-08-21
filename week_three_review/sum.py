'''
Find the sum of the even elements that are at odd indices
Input:
[1, 2, 3, 4, 5, 6, 7]
Output:
12

Input:
[1, 2, 8, 3, 9, 4]
Output:
6

'''
def sum_number(array):

    sum=0
    for i in range(len(array)):
        if i%2 !=0:
            if array[i]%2==0:
                sum +=array[i]

    return sum

list1=[1, 2, 3, 4, 5, 6, 7]
list2=[1, 2, 8, 3, 9, 4]

print(sum_number(list1))
print(sum_number(list2))
