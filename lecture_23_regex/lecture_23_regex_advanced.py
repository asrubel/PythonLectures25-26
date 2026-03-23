import re

print(re.match('\\\\', '\\'))

regexp = '[bd]a[td]'
print("Template -> ", regexp)
print(re.match(regexp, "bat"))
print(re.match(regexp, "dad"))
print(re.match(regexp, "cat"))
print(re.match(regexp, "bot"))

regexp = 'ja[a-z]'
print("Template -> ", regexp)
print(re.match(regexp, "jazz"))
print(re.match(regexp, "jam"))
print(re.match(regexp, "jaZ"))
print(re.match(regexp, "ja1"))

regexp = '[A-Z]ill'
print("Template -> ", regexp)
print(re.match(regexp, "Bill"))
print(re.match(regexp, "bill"))
print(re.match(regexp, "1ill"))

regexp = '[2-8a-c!?A-Q]'
print("Template -> ", regexp)
print(re.match(regexp, "Z"))
print(re.match(regexp, "d"))
print(re.match(regexp, "1"))
print(re.match(regexp, "?"))
print(re.match(regexp, "B"))
print(re.match(regexp, "!"))

regexp = '[^A-C]'
print("Template -> ", regexp)
print(re.match(regexp, "Z"))
print(re.match(regexp, "A"))

regexp = '[A-C^]'
print("Template -> ", regexp)
print(re.match(regexp, "Z"))
print(re.match(regexp, "A"))
print(re.match(regexp, "^"))

regexp = '[\\w]'
# regexp = '[\\W]'
# regexp = '[\\d]'
# regexp = '[\\D]'
print("Template -> ", regexp)
print(re.match(regexp, "A"))
print(re.match(regexp, "b"))
print(re.match(regexp, "1"))
print(re.match(regexp, "?"))
print(re.match(regexp, "B"))
print(re.match(regexp, "!"))

regexp = 'wo+w!'
print("Template -> ", regexp)
print(re.match(regexp, "wow!"))
print(re.match(regexp, "woooooooooow!"))
print(re.match(regexp, "ww!"))
print(re.match(regexp, "wiiiw!"))

regexp = 'Python [1-9]+'
print("Template -> ", regexp)
print(re.match(regexp, "Python 11111111"))
print(re.match(regexp, "Python 1234567890"))
print(re.match(regexp, "Python "))

regexp = 'go*d'
print("Template -> ", regexp)
print(re.match(regexp, "god!"))
print(re.match(regexp, "goooooooood!"))
print(re.match(regexp, "gd!"))

regexp = '.*no.*'
print("Template -> ", regexp)
print(re.match(regexp, "no"))
print(re.match(regexp, "no!!!!! please no!!!"))
print(re.match(regexp, "I have no explanation"))

regexp = '\\w{5}'
print("Template -> ", regexp)
print(re.match(regexp, "no"))
print(re.match(regexp, "noooo"))
print(re.match(regexp, "no oooo"))

regexp = '\\d{5,10}'
print("Template -> ", regexp)
print(re.match(regexp, "1234"))
print(re.match(regexp, "123456"))
print(re.match(regexp, "1234567890"))
print(re.match(regexp, "12345678900000"))

regexp = '(h[ao]){2}'
print("Template -> ", regexp)
print(re.match(regexp, "ha"))
print(re.match(regexp, "ho"))
print(re.match(regexp, "haho"))
print(re.match(regexp, "haha"))
print(re.match(regexp, "hoh"))

regexp = '(java|python|C#)'
print("Template -> ", regexp)
print(re.match(regexp, "java"))
print(re.match(regexp, "python"))
print(re.match(regexp, "C++"))

regexp = '(\\+38|^)0(66|67|68|95|96|97|98|99)\\d{7}'
print("Template -> ", regexp)
print(re.match(regexp, "+380986667788"))
print(re.match(regexp, "+3809866677889"))
print(re.match(regexp, "+38098666778"))
print(re.match(regexp, "+380916667788"))
print(re.match(regexp, "+381986667788"))
print(re.match(regexp, "+480986667788"))
print(re.match(regexp, "0986667788"))
