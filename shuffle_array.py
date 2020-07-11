import random


def shuf(a):
    narr = arr[:]
    random.shuffle(narr)
    print("Orignal Array: \n{}".format(arr))
    print("Shuffled Array: \n{}".format(narr))


arr = [1,2,3,4,5]

shuf(arr)
