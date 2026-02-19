# Write a program to find out whether a given post is talking about "Jordan" or not

# post = "Hey JorDAn bro is good joRdan is very good and JOrdAn is great"
post = input("Enter the post: ")

if("Jordan".lower() in post.lower()):
    print("This post is talking about Jordan")

else:
    print("This post is not talking about Jordan")