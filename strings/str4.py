'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : "resta$t" '''

string1 = "restart"

repl_str = string1[:1]

op_str = ""

for ch in string1:
    if ch not in op_str:
        op_str = f"{op_str}{ch}"
    elif repl_str == ch:
        op_str = op_str + "$"
    else:
        op_str = f"{op_str}{ch}"

print(op_str)


print("..................XXXXXXXXXXXXX....................")

other_str = string1[1:]

if repl_str in other_str:
    other_str = other_str.replace(repl_str, "$")

print(repl_str + other_str)
