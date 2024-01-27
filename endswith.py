#!/usr/bin/python

str_example = "this is string example .......wow!!!"

suffix = "wow!!!"
print(str_example.endswith(suffix))
print(str_example.endswith(suffix, 20))

suffix = "is"
print(str_example.endswith(suffix, 2, 4))
print(str_example.endswith(suffix, 2, 6))

