''''
Remove and print every third number from a list of numbers until the list becomes empty
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
30
60
90
40
80
50
20
70
10

'''

def remove_third_element(array):
    
    index=2
    removed_list=[]
    while array:
        if index<=len(array):
            remove=array.pop(index)
            removed_list.append(remove)

        if array:
            index=(index+2)%len(array)

        else:
            index=0

    return removed_list

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
list=remove_third_element(nums)
for i in list:
    print(i)


