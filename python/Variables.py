a = 1   # global variables 
print(a)
def fun(): # any variable which is initialized inside a function/class is called local variable
    b = 2   
    print("invoked inside the function:",a)  # this will work because a is a global variable and can be accessed inside the function
    print(b)

fun()
print(a)
print("b is invoked outside the function:",b)  