'''
Find the even-length words and sort them by length
Input:
['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
Output:
['Pink', 'Orange']

'''

def even_string(array):
    
    list=[]
    n=len(array)
    for i in range(n):
        if len(array[i])%2==0:
            list.append(array[i])

    return list

array_list=['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
print(even_string(array_list))