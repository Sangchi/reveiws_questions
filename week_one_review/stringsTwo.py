'''
reverse char in string

"I am a data engineer"
I ma a atad reenigne"

'''

def reverse_string(string):

    result = ""
    words = string.split()
    print(words)
    
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        result += reversed_word + " "

    return result


user_input = input("Enter the string: ")
print(reverse_string(user_input))
