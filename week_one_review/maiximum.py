#Find the maximum element in an array.

def maximum_element(array):
    
    max=array[0]
    n=len(array)
    for i in range(n):
        if array[i] > max:
            max=array[i]

    return max

item_array=[2,3,4,6,7,9,12]
print(maximum_element(item_array))
