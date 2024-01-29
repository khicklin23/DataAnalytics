def returnCommonValues(dict):
    values = list(dict.values())

    set_values = list(set(values))

    for element in set_values:
        if element in values:
            values.pop(values.index(element))
    print(set(values))



returnCommonValues({1:1,2:3,3:4,4:4,5:2,6:7,7:6,8:6,9:2,10:3,11:3})