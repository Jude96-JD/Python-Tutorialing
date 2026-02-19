for i in range(100):
    if(i == 38):
        break # exits the loop now
    print(i) # will print till 37 as the count starts from 0

for i in range(100):
    if(i == 38):
        continue # Skip this iteration
    print(i) # will not print 38, continues with 39