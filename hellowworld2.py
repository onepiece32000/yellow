#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 'Hello'
b = 'Python'

print("a + b output:", a + b)
print("a * 3 output:", a * 3)
print("a[1] output:", a[1])
print("a[1:4] output:", a[1:4])

if "H" in a:
    print("H changes a")
else:
    print("H does not change a")

if "M" not in a:
    print("M does not change a")
else:
    print("M changes a")

print(r'\n')  # r'\n' will print \n as a raw string
print(R'\n')  # R'\n' is the same as r'\n' in this context

