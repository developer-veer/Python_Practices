# read file from system
file = open("content.txt", 'r')

# read file data and store in a single string
# fileData = file.read()

# read line by line data from file
# line = file.readline()
with open('content.txt', 'r') as file:
    # Read the first 40 characters
    first_40_chars = file.read(40)
    print(first_40_chars)

with open("content.txt", 'r') as file_2:
    lines = file_2.readlines()  # readlines return list of lines
    for lin in lines:
        print(f'{lin[:10]} \n')  # this line print the first 10 characters of every line
# print(fileData)
# file.close()
