def letter_histogram(word):
    letterCount = {}
    for letter in word:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    return letterCount
print(letter_histogram("bananas"))



def word_histogram(paragraph):
    wordCount = {}
    paragraph = paragraph.lower().split()
    for word in paragraph:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount
print(word_histogram("To Be or not to be"))

def run():
    sentence = str(input("Write a sentence:  "))
    w_hist = word_histogram(sentence)
    count = make_count(w_hist)
    s_list = sort_most(count)
    print("The following words were used the most:", new_sort(s_list, count))


