'''Write a Python function that takes a list of words and return the longest word and the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9'''

list_words = ["word", "Exercises", "Exercise", "function"]

def lon_word(list_words):
    long_word = ""
    for wrd in list_words:
        if len(wrd) > len(long_word):
            long_word = wrd
    return long_word

print("Longest word: ",lon_word(list_words))
print("Length of the longest word: ", len(lon_word(list_words)))
