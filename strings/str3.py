'''Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''

list1 = ['w3resource', 'w3', ' w']

for item1 in list1:
    item1 = item1.replace(" ", "")
    if len(item1) < 2:
        print("Empty string")
    else:
        print(item1[:2]+item1[-2:])

