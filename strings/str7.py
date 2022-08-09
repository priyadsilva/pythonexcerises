'''Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : "The lyrics is not that poor!"
"The lyrics is poor!"
Expected Result : "The lyrics is good!"
"The lyrics is poor!"'''

string1 = "The lyrics is not that poor!"
string2 = "The lyrics is poor!"

str1not = string1.find("not")
str1poor = string1.find("poor")

str2not = string2.find("not")
str2poor = string2.find("poor")

if str1not < str1poor and str1not > 0 and str1poor > 0:
    string1 = string1[0:str1not] + "good" + string1[str1poor+4:]
    

if str2not < str2poor and str2not > 0 and str2poor > 0:
    string2 = string2.replace(string2[str2not:(str2poor+4)], "good")
    
print(string1)
print(string2)
