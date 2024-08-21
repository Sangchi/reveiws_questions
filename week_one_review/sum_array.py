#Calculate the sum of all elements in an array.

def sum_array(array):
    
    sum=0
    n=len(array)
    for i in range(n):
        sum +=array[i]

    return sum

item_array=[2,3,4,6]
print(sum_array(item_array))