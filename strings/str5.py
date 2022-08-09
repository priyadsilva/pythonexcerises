'''Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : "abc", "xyz"
Expected Result : "xyc abz"'''

string1 = "abc"
string2 = "xyz"

string12 = string2[:2] + string1[-1:]
string21 = string1[:2] + string2[-1:]

print(string12+" "+string21)
