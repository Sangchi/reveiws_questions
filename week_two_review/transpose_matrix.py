'''
Input =>Original Matrix :
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Output =>
```
Transpose matrix
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

'''


def transpose_matrix(list):

    list1=[]
    n=len(list)
    for row in range(n):
        new_list=[]
        for col in range(n):
            new_list.append(list[col][row])

        list1.append(new_list)

    return list1


def input_matrix():
    matrix = []
    list_cout = int(input("enter the number of rows: "))
    for i in range(list_cout):
        row = list(map(int, input(f"enter the numbers for row {i+1}, separated by spaces: ").split()))
        matrix.append(row)
    return matrix
matrix=input_matrix()
print(transpose_matrix(matrix))
