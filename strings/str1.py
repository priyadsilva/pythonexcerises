#Write a Python program to calculate the length of a string.
string1 = "Hello from Jupyter"
print("The lenght of string is: ", len(string1))

print("..................XXXXXXXXXXXXX....................")

def strlen(string1):
    count = 0
    for ch in string1:
        count = count + 1
    return count

strlen = strlen(string1)

print("The lenght of string is: ", strlen)
