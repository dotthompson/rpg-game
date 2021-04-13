# 1. Create a dictionary called zodiac with the following inforation.
# Each key is the name of the zodiac
zodiac = {
"Aries": "The Warrior",
"Taurus": "The Builder",
"Gemini": "The Messenger",
"Cancer": "The Mother",
"Leo": "The King",
"Virgo": "The Analyst",
"Libra": "The Judge",
"Scorpio": "The Magician",
"Sagittarius": "The Gypsy",
"Capricorn": "The Father",
"Aquarius": "The Thinker",
"Pisces": "TheMystic"
}

result = zodiac["Aries"]
print(result)


# 1a. Retrieve information about your zodiac from the zodiac dictionary

# 2. Given the following dictionary
phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
phonebook_dict["Kareem"] = "938-489-1234"
print(phonebook_dict["Elizabeth"])


# 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# 2c. Delete Alice's phone entry.
del phonebook_dict ["Alice"]
# 2d. Change Bob's phone number to '968-345-2345'.
phonebook_dict["Bob"] = "968-345-2345"

print(phonebook_dict)
# 2e. Print all the phone entries.

# 3. Nested dictionaries
keys = phonebook_dict.keys()
print(keys)
values = phonebook_dict.values()
print(values)

ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
} 
# 3a. Write a python expression that gets the email address of Ramit.
print(ramit['email'])
# 3b. Write a python expression that gets the first of Ramit's interests.
print(ramit['interests'][0])
# 3c. Write a python expression that gets the email address of Jasmine.
print(ramit['friends'][0]['email'])
# 3d. Write a python expression that gets the second of Jan's two interests.
print(ramit['friends'][1]['interests'][1])


# 4. Letter Summary
# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:
# >>>letter_histogram('banana')

word = input("Please type any word >>> ")
frequency = {}

for letter in word:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1
print("The character count for your word is  " + str(frequency))


# {'a': 3, 'b': 1, 'n': 2}
# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:
# >>> word_histogram('To be or not to

paragraph = input("Please type several sentences to be reviewed >>> ")


def wordCount(paragraph):
    wordCounter = {}
    wordList = paragraph.lower().split()
    for word in wordList:
        if word in wordCounter:
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
        
    return wordCounter

print(wordCount(paragraph))
