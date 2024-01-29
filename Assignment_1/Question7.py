# For use of list size 3
# For bigger lists, declare more "delete" variables and add more if checks
# Change chosenGivenValue variables to change the desired removal value
chosenGivenValue = "Kind"
chosenGivenValue2 = "Evil"
tupList = [("This", "List", "Is", "Evil"),("This", "Thing", "Has", "Given", "Me", "Trouble"),("This", "List", "Is", "Kind")]
tupList2 = [("A", "Kind", "Man"), ("An", "Evil", "Squirrel"), ("Dogs", "Are", "Kind")]
tupList3 = [("This", "List", "Is", "Evil"),("This", "Thing", "Has", "Given", "Me", "Trouble"),("This", "List", "Is", "Kind")]
tupList4 = [("A", "Kind", "Man"), ("An", "Evil", "Squirrel"), ("Dogs", "Are", "Kind")]
def listSearch(tupList, chosenGivenValue):
    print(f"Given Value: {chosenGivenValue}")
    print("Original List of Tuples:")
    print(tupList)
    print("\nNew List of Tuples:")
    delete1 = 0
    delete2 = 0
    delete3 = 0
    # Analyze tuples in list for value
    if (tupList[0].count(chosenGivenValue) > 0):
        delete1 = 1
    if (tupList[1].count(chosenGivenValue) > 0):
        delete2 = 1
    if (tupList[2].count(chosenGivenValue) > 0):
        delete3 = 1

    # Delete chosen entries in descending order to avoid indexing errors
    if (delete3 == 1):
        tupList.remove(tupList[2])
    if (delete2 == 1):
        tupList.remove(tupList[1])
    if (delete1 == 1):
        tupList.remove(tupList[0])

    print(tupList)
listSearch(tupList, chosenGivenValue)
print("")
listSearch(tupList2, chosenGivenValue2)
print("")
listSearch(tupList3, chosenGivenValue2)
print("")
listSearch(tupList4, chosenGivenValue)
print("")