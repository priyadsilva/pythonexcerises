'''Write a Python program to remove the nth index character from a nonempty string.'''

def remove_char(string1, index):
    if len(string1) < 0:
        print("string empty")
    else:
        return string1.replace(string1[index], '')

def remove_char2(string1, index):
    if len(string1) < 0:
        print("string empty")
    else:
        str1 = string1[:index]
        str2 = string1[index+1:]
        return str1+str2

        
print(remove_char("Python", 0))
print(remove_char("Python", 5))

print("..................XXXXXXXXXXXXX....................")

print(remove_char2("Python", 3))
