# Write a program to mine a log file and find out whether it contains 'python'.

with open("logfile.txt") as f:
    content = f.read()

if("python" in content):
    print("The word Python is present in the content")

else:
    print("The word Python is not present in the content")