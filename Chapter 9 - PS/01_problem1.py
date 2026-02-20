# Write a program to read the text from given file 'poem.txt' and find out whether it contains the word 'Twinkle'

f = open("poem.txt")
content = f.read()
if("Twinkle" in content):
    print("The word Twinkle is present in the content")
else:
    print("The word Twinkle is not present in the content")

f.close()