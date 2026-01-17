# print ("hello world")

s = 'hi hEllo WORLD'
d = 'meet you'
# print(s[3])
# h

# print (len(s))
# 14

# print (s + ' ' + 'nice to' + ' ' + d)
# hi hello world nice to meet you

#F STRING
# print (f"{s} nice to {d}")
# hi hello world nice to meet you

pi = 3.14
text = 'The value of pi is ' + str(pi)
text = (f"{s} what is the value of pi? \n{text}")
# print(text)
# hi hello world what is the value of pi? 
# The value of pi is 3.14

raw = r'whatever\nI type\t will not matter'
nospace = """wherever I type
   it will always matter"""
# print (nospace)
# print(raw)
#whatever\nI type\t will not matter

print (s.lower())
# hi hello world
print (s.upper())
# HI HELLO WORLD
print (s.strip())