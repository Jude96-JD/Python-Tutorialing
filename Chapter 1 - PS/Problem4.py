# Write a python program to print the contents of a directory using the OS module

# OS module is basically for File & directory tasks such as list, view, move, delete, make new folder etc

import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)