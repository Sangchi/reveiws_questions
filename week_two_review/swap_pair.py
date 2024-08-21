'''
Input: [2, 5, 11, 30, 7 , 4, 66 , 13 , 34 , 89]
Output: [11, 30 , 2, 5 , 66, 13 , 7 , 4 , 34 , 89]

'''

def swap_pairs(array):
    swapped_list = []
    for i in range(0, len(array) - len(array) % 4, 4):
        swapped_list.append(array[i + 2])
        swapped_list.append(array[i + 3])
        swapped_list.append(array[i])
        swapped_list.append(array[i + 1])
    

    swapped_list.extend(array[len(swapped_list):])

    return swapped_list

array_list = [2, 5, 11, 30, 7, 4, 66, 13, 34, 89,90,21,23]
print(swap_pairs(array_list))
