#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print(type(n))
print(type(n) is int)
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
