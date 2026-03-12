import os

l1 = []
files = os.listdir('.')
print(files)

for i in files:
    if i.endswith('.py'):
        l1.append(i)

print(l1)

l2 = [file for file in os.listdir('.') if file.endswith(('.py', ".csv"))]
print(l2)

path = "/Users/premkumargontrand/AITrainingMar2026/python/modules"

if os.path.isfile(path):
    print("This is a file.")
elif os.path.isdir(path):
    print("This is a directory.")

path1 = "/Users/premkumargontrand/AITrainingMar2026/python/modules/pydantic.py"

dir1,file1 = os.path.split(path1)
print("Directory:", dir1)
print("File:", file1)

filename = "example,txt"
filename, extension = os.path.splitext(filename)
print("Filename:", filename)
print("Extension:", extension)

text = "Hello, how are you doing today?"
output1 = text.split(',')
print(output1)

workingdir = os.getcwd()

l6 = os.system("df -h")
print(l6)


