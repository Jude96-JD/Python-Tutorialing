friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]

print(friends)

friends.append("Jordan")

print(friends)

l1 = [1, 34, 62, 2, 6, 11]

# l1.sort() # Sorts the list in ascending order

# l1.reverse() # Reverses the list, like [11,6,2,62,34,1]

# l1.insert(3, 33333) # Insert 33333 such that its index in the list is 3

l1.remove(62) # Removes a list, as added 62 here will remove the 62 from the list

# value = l1.pop(3)
# print(value)
print(l1)

del l1 [0:2] # Although not related to this (or maybe is) i can delete multiple values in ratio [0:2] will remove 3 values, unlike l1.remove() which removes a singular list

print(l1)