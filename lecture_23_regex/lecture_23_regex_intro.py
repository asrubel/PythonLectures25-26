import re

# regexp = 'python'
# string = 'python'
# regexp = 'python'
# string = 'pytho'
regexp = 'PYTHON'
string = 'python'

print("Template -> ", regexp)
print("String -> ", string)
res = re.match(regexp, string)
print(res)

regexp = 'python .'
print("Template -> ", regexp)
print(re.match(regexp, "python "))
print(re.match(regexp, "python 2"))
print(re.match(regexp, "python 323333333"))
print(re.match(regexp, "python !"))
print(re.match(regexp, "------ python !"))

regexp = 'pytho?'
print("Template -> ", regexp)
print(re.match(regexp, "pytho"))
print(re.match(regexp, "python"))
print(re.match(regexp, "pytho3"))
print(re.match(regexp, "python3"))

regexp = 'pytho\\?'
print("Template -> ", regexp)
print(re.match(regexp, "pytho"))
print(re.match(regexp, "python"))
print(re.match(regexp, "pytho?"))
