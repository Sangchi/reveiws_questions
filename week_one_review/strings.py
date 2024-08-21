'''
take input from user and check vowels are present in string if vowels present make it upper case
and return result

'''

def capital_vowels(string):
 
    new_string=string.lower()
    vowels="aeiouAEIOU"
    result=""
    for char in new_string:
        if char in vowels:
            result +=char.upper()

        else:
            result +=char

    return result

user_input=input("enter your string:")
print(capital_vowels(user_input))


'''
output-
enter your string:bridgelabz
brIdgElAbz


'''