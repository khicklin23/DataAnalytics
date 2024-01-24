def split(input_list):
    #start with an empty list
    output_list = []
    
    for i in range(0, len(input_list), 2):
        #using odd items as keys
        key = input_list[i]
        
        #using even items as values
        value = input_list[i + 1]
        #create a list of dictionaries 
        output_list.append(dict({key: value}))
    
    return output_list

# Testing Case:
print(split([1, 'one', 2, 'two', 3, 'three', "Hello", "there", "General", "Kenobi", "key", "value", "taco", "burrito"]))
