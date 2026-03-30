# i = 10

# while i < 20:
#     print(i)
#     i += 1

# while i <= 20:
#     if i == 15:
#         print("i is equal to 15")
#         break

# while i < 20:
#     if i == 15:
#         print("i is equal to 15")
#         continue
#     print(i)
#     i += 1



# def func1(user_input):
#     print("You entered:", user_input) 



# while True:
#     user_input = input("Enter your text (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         print("Exiting the program.")
#         break
#     else:
#         func1(user_input)


# while True:
#     user_input = input("Enter your text (or 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         print("Exiting the program.")
#         break
    
#     if not user_input:
#         print("Input cannot be empty. Please try again.")
#         continue
#     else: 
#         func1(user_input)
    
# password_attempt = 0

# while password_attempt < 3:
#         password = input("Enter your password: ")
#         if password == "password123":
#             print("Access granted.")
#             break
#         else:
#             print("Incorrect password. Try again.")
#             password_attempt += 1
# else:
#         print("Disable-ADAccount -Identity 'username'")
#         print("Too many failed attempts. Access denied and account locked.") 

#one liner coding 
i = 10
while i < 20: print(i); i += 1
i =1
while i <= 10: print(2*i); i += 1

i = 10; 
if i < 20: print(i); i += 1

evennumber = [i for i in range(1, 21) if i % 2 == 0]
oddnumber = [i for i in range(1, 21) if i % 2 != 0]
adult = [{"age":20},{"age":17}]; adult_validation = [person for person in adult if person["age"] >= 18]
