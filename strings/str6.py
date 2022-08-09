'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : "abc"
Expected Result : "abcing"
Sample String : "string"
Expected Result : "stringly"'''

str_list = ["a", "abc", "string"]

for item in str_list:
    if len(item) < 3:
        print(item)
    else:
        if item[-3:] == "ing":
            print(item + "ly")
        else:
            print(item + "ing")
