#!/usr/bin/python3

def pascal_triangle(n):
	result = []
	i = 0
	while (i < n) :
		result.append([])
		i += 1
	if (n == 1):
		result[0][0] = 1
		return (result)
	elif (n == 2):
		result[0][0] = 1
		result[1][0] = 1
		result[1][1] = 1
		return(result)
	