# #Strings

# # concatenation
# name = "yujin"
# greeting = "hi"
# complete = name + greeting

# # repeat
# name_repeat = name * 2 #However many times you want the repetition

# # slicing
# slice = name[1:4]

# #How do we use negative indexing 
# i = name[0]
# print(i)
# #It starts from the end and the last character has an index of -1

# #Uppercase, lowercase and splitting

# w = "Hello world"
# w.split()
# name.upper()
# name.lower()

#string formatting

# name = "yujin"
# greeting = "hi"
# a = f"{greeting}, I am {name}"

# #length
# len(name)

# #presence
# "b" in name
# "b" not in name

#Handling of text files
# opened = open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\quotes.txt","r")
# content = opened.read()
# print(content)
# opened.close()

#Better
# with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\quotes.txt","r") as opened:
#    content = opened.read()
#    print(content)


#.readline(Takes in a parameter for the number of characters for the first line)
# with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\quotes.txt","r") as opened:
#    content = opened.readline(170)
#    print(content)

#write mode
# with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\demo_writing.txt","w") as a:
#     a.write("Demonstrating write mode in files")

# #append mode
# with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\demo_writing.txt","a") as new_words:
#     new_words.write("Demonstrating appending in files")

#task- create a file using the x mode, write a line to the file, open it again in append mode and add a new line, print the contents of appended file to confirm success

with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\task.txt","x") as task:
    task.write("This is the writting step in the task")

with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\task.txt","a") as task_addition:
    task_addition.write("This is the appending step in the task")

with open(r"C:\Users\SHADRACK\OneDrive\Desktop\Python-Programming\Week_2\task.txt","r") as task_read:
    reading = task_read.read()
    print(reading)





    






