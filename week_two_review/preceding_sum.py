'''
input:[7,2,11,29,51,6]
output:[7,9,13,40,80,57]

'''

def preceding_sum(array):

    result=[]
    result.append(array[0])
    for i in range(len(array)-1):
        sum=array[i]+array[i+1]
        result.append(sum)
        
    
    return result

array_list=[7,2,11,29,51,6]
print(preceding_sum(array_list))

'''
[7, 9, 13, 40, 80, 57]

'''