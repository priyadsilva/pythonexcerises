'''Write a Python program to change a given string to a new string where the first and last chars have been exchanged.'''

string1 = "Python"

print(string1[-1:] + string1[1:-1] + string1[:1])
