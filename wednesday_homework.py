# (1) Multiply Vectors
listA = [2, 4, 5]

listB = [2, 3, 6]

newList = [listA[0]*listB[0], listA[1]*listB[1], listA[2]*listB[2]]

print(newList)

# (2) Matrix Addition

listC = [[1, 3], [2, 4]]

listD = [[5, 2], [1, 0]]

newList2 = [[[listC[0][0] + listD[0][0], listC[0][1] + listD[0][1]]], [[listC[1][0] + listD[1][0], listC[1][1] + listD[1][1]]]]

print(newList2)

# (3) Matrix Addition II

x = [[12, 7, 3],
    [4, 5, 6], 
    [7, 8, 9]]


y = [[5, 8, 1], 
    [6, 7, 3],
    [4, 5, 9]]

result = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)

# (4) De-dup

mydupList = [2, 4, 3, 6, 6, 7, 2, 2, 4, 9, 8, 6, 4, 1, 9, 9, 11, 7, 1]
myfinaldupList = set(mydupList)
print(list(myfinaldupList))

# (5) Leetspeak

replacements = (('a', '4'), ('e', '3'), ('g', '6'), ('i', '1'), ('o', '0'), ('s', '5'), ('t', '7'))
my_paragraph = """ I need to translate this paragraph to leetspeak. 
I have no idea what leetspeak is or how to do it. Here goes nothing. """

new_paragraph = my_paragraph
for old, new in replacements:
    new_paragraph = new_paragraph.replace(old, new)

print(new_paragraph)

# (6) Long-long vowels

word = input('Enter word >>>   ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for letter in word:
    if letter in vowels:
        newWoooord = word + (letter*5)
print(newWoooord)

# (7) Ceasar Cypher

statement = "Every night when I sleep my brain takes over me"


cryptic_message = "lbh zhfg hayrnea jung lbh unir yrnearq"

offset = 13
alphabet1 ='abcdefghijklmnopqrstuvwxyz'
result = ''

for x in cryptic_message:
    caesar = ord(x)
    is_uppercase = caesar >= 65 and caesar <= 90
    x = x.lower()
    if x not in alphabet1:
        new_x = x
    else:
        idx = alphabet1.find(x)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
        new_x = alphabet1[new_idx]
        if is_uppercase:
            new_x = new_x.upper()

    result += new_x

print(result)