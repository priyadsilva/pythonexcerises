'''Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}'''

string1 = "google.com"

dict1 = {}

for ch in string1:
    if ch in dict1.keys():
        dict1.update({ch : dict1[ch] + 1})
    else:
        dict1.update({ch : 1})
print(dict1)
