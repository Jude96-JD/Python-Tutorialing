# Write a program to print the following start pattern:
'''
*
**
*** for n = 3
'''

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*"* i, end="")
    print("") # blank by default gives a new line