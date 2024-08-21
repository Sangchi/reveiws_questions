def minimum_element(array):
    
    min=array[0]
    n=len(array)
    for i in range(n):
        if array[i] < min:
            min=array[i]

    return min

item_array=[2,3,4,5,6]
print(minimum_element(item_array))

        