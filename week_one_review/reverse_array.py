#Reverse an array.

def array_reverse(array):
    reverse=[]
    start=-1
    n=len(array)-1
    for i in range(n,start,-1):
        reverse.append(array[i])

    return reverse

item_array=[2,3,4,5,6]
print(array_reverse(item_array))

'''
output-
[6, 5, 4, 3, 2]

'''

