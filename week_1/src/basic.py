#!/usr/bin/python
# -*- coding: utf-8 -*-

# 변수 (variable) 사용법

# int
a = 3
b = 5
print(a + b)

# float
a = 3.5
b = 2.5
print(a - b)

# string
a = "hi"
b = 'hi'
print(a)
print(b)

# 리스트 (List) 사용법
a = [1, 2, 3, 4, 5]
print(a, len(a))

b = ["a", "b", "c", "d"]
print(b, len(b))

c = [1, "a", 2.5]
print(c, len(c))


# dictionary 사용법
name_to_age = {
    "Jenny": 20
}
name_to_age["John"] = 26
name_to_age["Tom"] = 29
print(name_to_age["Jenny"])
print(name_to_age["John"])
print(name_to_age["Tom"])

name_to_age["Jenny"] = 21
print(name_to_age["Jenny"])


# function 사용법
def sum(a, b):
    return a + b


print(sum(3, 5))
print(sum(2, 1))


def sum_and_mul(a, b):
    return a + b, a*b

print(sum_and_mul(3, 5))
print(sum_and_mul(2, 1))
