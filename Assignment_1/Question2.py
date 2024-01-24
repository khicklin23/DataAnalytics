a = [1, 2, 3, 4, 5, 'a']
b = [4, 5, 6, 7, 8, 3, 'a']
match = len((set(a).intersection(b)))
print(match)
