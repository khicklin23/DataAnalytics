def combine_dictionaries(dict1, dict2):
    combined_dict = {}

    # Combine dictionaries based on keys using union 
    for key in set(dict1.keys()).union(dict2.keys()):
        combined_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

    return combined_dict

# Dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30, 'e': 13}
dict2 = {'b': 5, 'c': 15, 'd': 25, 'e': 27}

# Combine dictionaries
print(combine_dictionaries(dict1, dict2))
