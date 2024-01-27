#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

print("Random number without seed:", random.random())
print("Random number without seed:", random.random())

print()

random.seed(10)
print("Random number with seed 10:", random.random())

random.seed(10)
print("Random number with seed 10:", random.random())

random.seed(10)
print("Random number with seed 10:", random.random())

