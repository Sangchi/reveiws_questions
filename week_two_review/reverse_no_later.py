'''
Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.
Original list:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE']

'''

# def reverse_no_later(array):

#     for i in range(len(array)):

#         if array[i].isdigit():
#             array[i] = array[i][::-1]
#         else:
#             array[i] = array[i].upper()
#     return array


# array_list = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
# print(reverse_no_later(array_list))


'''
Find the sum of the even elements that are at odd indices
Input:
[1, 2, 3, 4, 5, 6, 7,8]
Output:

'''

# def odd_index_evennumber_sum(array):

#     n=len(array)
#     sum=0
#     for i in range(n):
#         if i%2 !=0:
#             if array[i]%2==0:
#                 sum +=array[i]

#     return sum

# array_list=[1, 2, 3, 4, 5, 6, 7,8]
# arry=[1, 2, 8, 3, 9, 4]
# print(odd_index_evennumber_sum(array_list))
# print(odd_index_evennumber_sum(arry))

'''
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

# def remove_third_number(array):

#     list=[]
#     index=2

#     while array:

#         if index<=len(array):
#             remove_element=array.pop(index)
#             list.append(remove_element)

#         if array:
#             index=(index+2)% len(array)

#         else:
#             index=0

#     return list

# array_list=[10, 20, 30, 40, 50, 60, 70, 80, 90]

# result=remove_third_number(array_list)
# for element in result:
#     print(element)

'''
Write a Python function that accepts a string and counts the number of upper and lower case letters.
Original String :  The quick Brow Fox
No. of Upper case characters :  3
No. of Lower case Characters :  13

'''

# def upper_and_lower_count(string):
    
#     count1=0
#     count2=0
#     new_string=string.strip()

#     for char in new_string:

#         if char.isupper():
#             count1 +=1

#         else:
#             count2 +=1
    

#     print(f"upper count is:{count1}")
#     print(f"the lower count is {count2}")

# string_latter="The quick Brow Fox"

# print(upper_and_lower_count(string_latter))

'''
Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".

'''

# def demo(number):

#     if number==3:
#         return "Fizz"
#     elif number==5:
#         return "Buzz"

#     else:
#         return "FizzBuzz"
    

# num=int(input("enter the number:"))

# print(demo(num))

'''
Reverse Integer:
Input= 123
output: 321
Input: -4576
output: -6754


'''

# def reverse_intiger(number):

#     if number<=0:
#         return False
    
#     original_num=number
#     reversed_number=0

#     while number>0:
#         digit=number %10
#         reversed_number=reversed_number*10+digit
#         number//=10

#     return reversed_number

# number=int(input("enter the number:"))
# print(reverse_intiger(number))






