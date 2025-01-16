#This is how you would open a file normally, always remember to use file.close()

# file = open(r"C:\Users\brent\OneDrive\Desktop\Python Coding Learning\100 days Challenge\100-Days-of-Python-Course\Intermediate_day15-44\Day 24 Read and write\myfile.txt")
# content = file.read()
# print(content)
# file.close()

#This is how you open a file with the "with open"
# with open(r"C:\Users\brent\OneDrive\Desktop\Python Coding Learning\100 days Challenge\100-Days-of-Python-Course\Intermediate_day15-44\Day 24 Read and write\myfile.txt") as file:
#     content = file.read()
#     print(content)

#This is how you would overwrite a file with new text#

# with open(r"C:\Users\brent\OneDrive\Desktop\Python Coding Learning\100 days Challenge\100-Days-of-Python-Course\Intermediate_day15-44\Day 24 Read and write\myfile.txt", "w") as file:
#     file.write("new text.")
    
    
    #This his how you would append text to the end of a text file rather than overwriting it
# with open(r"C:\Users\brent\OneDrive\Desktop\Python Coding Learning\100 days Challenge\100-Days-of-Python-Course\Intermediate_day15-44\Day 24 Read and write\myfile.txt", "a") as file:
#     file.write("\nnew text.")

with open("new_file1.txt", mode="w") as file:
    file.write("Hello")