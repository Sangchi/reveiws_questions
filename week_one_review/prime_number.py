# import math
# def prime_number(number):

#     if number<=1:
#         return False
#     if number==2:
#         return True
#     if number%2==0:
#         return False
    
#     # limit=int(math.sqrt(number)+1)

#     for i in range(3,int(number ** 0.5) +1,2):
#         if number%i==0:
#             return False
        
#     return True

# user=int(input("enter the number:"))
# if prime_number(user):
#     print(f"{user}is prime number")

# else:
#     print(f"{user} is not the prime number")
