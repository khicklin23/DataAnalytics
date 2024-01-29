# Since not specified, I created an example using 3 tuples of size 3.
# Add or remove prints and elifs for different size/amount of tuples
#

t1 = [3, 5, 7]
t2 = [49, 14, 56]
t3 = [10, 2, 3]
t4 = [5, 5, 6]
t5 = [39, 64, 6]
t6 = [1, 6, 5]
t7 = [6534, 211, 567]
t8 = [493, 4, 560]
t9 = [100, 2, 3]

# For 3 tuples of size 3
def sortUnsort(tuple1, tuple2, tuple3):
    print("Unsorted:")
    print(tuple1)
    print(tuple2)
    print(tuple3)
    print("")
    print("Sorted:")
    if ((tuple1[0] < tuple2[0]) & (tuple1[0] < tuple3[0])): # If tuple1 is smallest
        print(tuple1)
        if (tuple2[0] < tuple3[0]):
            print(tuple2)
            print(tuple3)
        elif (tuple3[0] < tuple2[0]):
            print(tuple3)
            print(tuple2)
        elif (tuple3[0] == tuple2[0]):
            if (tuple2[1] < tuple3[1]):
                print(tuple2)
                print(tuple3)
            elif (tuple3[1] < tuple2[1]):
                print(tuple3)
                print(tuple2)
            elif (tuple3[1] == tuple2[1]):
                if (tuple2[2] < tuple3[2]):
                    print(tuple2)
                    print(tuple3)
                elif (tuple3[2] < tuple2[2]):
                    print(tuple3)
                    print(tuple2)
                elif (tuple3[2] == tuple2[2]):
                    print(tuple2)
                    print(tuple3)
    elif ((tuple2[0] < tuple1[0]) & (tuple2[0] < tuple3[0])): # If tuple2 is smallest
        print(tuple2)
        if (tuple1[0] < tuple3[0]):
            print(tuple1)
            print(tuple3)
        elif (tuple3[0] < tuple1[0]):
            print(tuple3)
            print(tuple1)
        elif (tuple3[0] == tuple1[0]):
            if (tuple1[1] < tuple3[1]):
                print(tuple1)
                print(tuple3)
            elif (tuple3[1] < tuple1[1]):
                print(tuple3)
                print(tuple1)
            elif (tuple3[1] == tuple1[1]):
                if (tuple1[2] < tuple3[2]):
                    print(tuple1)
                    print(tuple3)
                elif (tuple3[2] < tuple1[2]):
                    print(tuple3)
                    print(tuple1)
                elif (tuple3[2] == tuple1[2]):
                    print(tuple1)
                    print(tuple3)
    elif ((tuple3[0] < tuple2[0]) & (tuple3[0] < tuple1[0])): # If tuple3 is smallest
        print(tuple3)
        if (tuple2[0] < tuple1[0]):
            print(tuple2)
            print(tuple1)
        elif (tuple1[0] < tuple2[0]):
            print(tuple1)
            print(tuple2)
        elif (tuple1[0] == tuple2[0]):
            if (tuple2[1] < tuple1[1]):
                print(tuple2)
                print(tuple1)
            elif (tuple1[1] < tuple2[1]):
                print(tuple1)
                print(tuple2)
            elif (tuple1[1] == tuple2[1]):
                if (tuple2[2] < tuple1[2]):
                    print(tuple2)
                    print(tuple1)
                elif (tuple1[2] < tuple2[2]):
                    print(tuple1)
                    print(tuple2)
                elif (tuple1[2] == tuple2[2]):
                    print(tuple2)
                    print(tuple1)
    else: # If all three start with the same element
        print(tuple1)
        print(tuple2)
        print(tuple3)
print("Tuples 1, 2, & 3")
sortUnsort(t1, t2, t3)
print("")
print("Tuples 4, 5, & 6")
sortUnsort(t4, t5, t6)
print("")
print("Tuples 7, 8, & 9")
sortUnsort(t7, t8, t9)
print("")
print("Tuples 4, 7, & 1")
sortUnsort(t4, t7, t1)
print("")
print("Tuples 2, 5, & 8")
sortUnsort(t2, t5, t8)
print("")
print("Tuples 1, 9, & 3")
sortUnsort(t1, t9, t3)
print("")
print("Tuples 1, 1, & 1")
sortUnsort(t1, t1, t1)
print("")