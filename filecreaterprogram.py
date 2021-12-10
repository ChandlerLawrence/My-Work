#Here I am importing the os library/module to use in my program below
import os
#Here I am prompting the user for the name of the directory of their choice
directory_name = input('Enter in the directory of your choice: ')
#Here I am using an if statement to create a directory if that one chosen directory doesn't already exists
if os.path.isdir(directory_name) is False:
    os.mkdir(directory_name)
#Here I am prompting the user for the name of their file
file_name = input('Enter in the name of your file: ')
#Here I have created the file path based upon the user's directory and file name of choice into a text document
file_path = os.path.join(directory_name, file_name +".txt")
#Here I am creating the file
your_file = open(file_path, "x")
#Here I am prompting the user to input their name, address and phone number
name = input("Enter in your first and last name: ")
address = input("Enter in your street address: ")
phone_number = input("Enter your phone number: ")
#Here I have joined all values together from the user's input as a line of comma seperated values
output = name, address, phone_number
#Here I am writing that data as a string to the file
your_file.write(str(output))
#Here I have closed the file to save the changes
your_file.close()
#Here I have opened the file and displayed the contents to the user as program output
with open(file_path, "r") as file:
    contents = file.read()
    print(contents)
#Here I am closing the file
your_file.close()
#End of program

