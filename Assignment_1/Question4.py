a = ['data', 'analysis', 'programming', 'python', 'jupyter']

# use list comprehension to create a list that contains the lengths of the strings in a.
newlist = [len(x) for x in a]
longIndex = newlist.index(max(newlist))  # index of longest string
longString = a[longIndex]                # get longest string
print("Longest string: " + longString)
print("Length of string: ", len(a[longIndex]))
