

# inbuild function - print() , input() , len() , type() , int() , str() , float() , list() , dict() , set() , tuple() , range() , etc.
# module function -  , datetime.now() , os.listdir() , sys.exit() , etc.
# custom function 

def func1():
    print("this is a function") 
    
print("this is a function")  # this is a statement

func1()


def func2(name:str="mahesh"):  # name= sam or arun or daniel
    print("Hello, " + name + "! Welcome to Python programming.")


func2("sam")
func2("arun")
func2("daniel")
func2()

def func3(username:str="mahesh",id:int=1):   # argument with default value and multiple argument
    print(f"Username: {username}, ID: {id}")



func3("daniel", 3)
func3()

def func4(*args):    # Low level coding *args and **kwargs - thread, process, looping   m
    print("Positional arguments:", args)

func4(1, 2, 3, "hello", [1, 2, 3])

# { name: "kumar", age: 30, city: "New York" } 

l1 = [1,2,3,4,] # this is a dictionary in python and json format


# function coding for add, sub, division and multiplication , single function doing all the actions 

function with if condition ( add , sub, div, mul) and function with if condition and return statement