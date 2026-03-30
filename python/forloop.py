# for i in range(0,10):
#     print(i)

# # for loop with list of value  
# # for with range function 
# # for with if condition 
# # for with nested loop and try except block
# # for loop will be called within a function and function will be called within for loop

# for i in range(0,10):
#     if i == 5:
#         print("i is equal to 5")
#         continue 
#     print(i)


# for i in range(0,10):
#     if i == 5:
#         break
#     print(i)
# else:
#     print("loop completed successfully")

text = "Hello, World! i am learning python, PYTHON is a great programming language."
count = 0
for i in text:
    if i =='l':
        count += 1
print("The letter 'l' appears", count, "times in the text.")

l1 = []
for word in text.split(","):
    # print(word)
    l1.append(word)
print(l1)
l2 = []
for word in text.split():
    cleaned_word = word.strip(",.!?").lower()  # Remove punctuation
    l2.append(cleaned_word)
print(l2)

inputlines =   """
This is the first line.
This is the second line.        

This is the third line.
    """
for line in inputlines.splitlines():
    if line.strip():  # Check if the line is not empty
        print(line.strip())

# with for - split, splitlines, strip 

# prompt - max_token, empty space, security violation (password, email , admin, format), summarization  or rewriting the prompt

