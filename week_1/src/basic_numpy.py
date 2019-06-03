#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy

list_matrix = [[1, 2, 3], [3, 6, 9], [2, 4, 6]]
matrix = numpy.array(list_matrix)

print(matrix)
print(matrix.shape)

print(matrix[1, 2])
print(matrix[1])
print(matrix[1: 3])
print(matrix[:, 1])

matrix = matrix + 3
print(matrix)

matrix = matrix + matrix
print(matrix)

for i in range(3):
    matrix = numpy.random.rand(3, 3)
    print(i, matrix)

matrix = numpy.zeros((3,3))
print(matrix)


list_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix1 = numpy.array(list_matrix)

matrix2 = numpy.array([1, 2, 3])

print(matrix1*matrix2)
print(numpy.dot(matrix1, matrix2))
