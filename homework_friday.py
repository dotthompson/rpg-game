# (1) Find the smallest number

listNum = [12, 23, 4, 7, 32, 8, 18, 9]

def smallestNum():
    listNum.sort()
    print(listNum[0])

smallestNum()

# (2) Find largest number

def largestNum():
    listNum.sort()
    print(listNum[7])

largestNum()

# (3) Find the shortest string

stringA = "I like to code."
stringB = "Coding is hard though."

def shortest(x, y):
    if len(x) < len(y):
        print(x)
    else:
        print(y)

shortest(stringA, stringB)

# (4) Find the longest string

def longest(x, y):
    if len(x) > len(y):
        print(x)
    else:
        print(y)

longest(stringA, stringB)


