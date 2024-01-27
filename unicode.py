#!/usr/bin/python3

#s = '²3455'
s = '\u00B23455'
print(s.isnumeric())
# s = '½'
s = '\u00BD'
print(s.isnumeric())

a = "\u0030" #unicode for 0
print(a.isnumeric())

b = "\u00B2" #unicode for ²
print(b.isnumeric())

c = "10km2"
print(c.isnumeric())
