# # if with function coding 
# # if with regular expression
# # if with logical operator -  and , or , not , ==, >, <, >=, <=, !=
# # if with try except block, for and while loop 

a = 10
b = 20
c = 30
if a > b:
    print("a is greater than b")

if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")

if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")

if b >= 18:
    print("b is an adult")
else:
    print("b is a minor")

# and operator, or opertor , not operator, combination of both 
if a > b and a > c:
    print("a is the greatest")
elif b > a and b > c:
    print("b is the greatest")
elif c > a and c > b:
    print("c is the greatest")
else:
    print("a, b and c are equal")

import sys
import logging

logging.basicConfig(filename='access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
user_list = ["admin", "root", "superuser"]
username = input("Enter your username: ")

if not user_list:
    print("Username cannot be empty")
    sys.exit(1)

if username not in user_list:
    print("Access granted to the system")
else:
    print("Access denied to the system")
    logging.error("Unauthorized access attempt by user: %s", username)
    sys.exit(1)


# if condition within a function  or function called within if condition

def user_validation(username: str= "kumar"):
    user_list = ["admin", "root", "superuser"]
    if not username:
        print("Username cannot be empty")
        sys.exit(1)

    if username not in user_list:
        print("Access granted to the system")
    else:
        print("Access denied to the system")
        sys.exit(1)


usern = input("Enter your username: ")
user_validation(usern)

prompt = input("Enter your query: ")
if not prompt:
    print("Query cannot be empty")
    
if len(prompt) < 3:
    print("Query is too short")
elif len(prompt) > 100:      # optimizing the cost in model utilzation / max_token 
    print("Query is too long")
else:
    print("Query is valid")


# search -- > internal docs(0), model search($0.05), web search( model and web tool )($0.10)
search_query = input("Enter your search query: ")


docs = vectorstore.similarity_search(search_query, k=5) 

if not docs:
    response = model.chat(search_query)
else:
    response = model.tool.websearch()





