#################################################################
# Problem 1: https://projecteuler.net/problem=1
# STATEMENT: If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
#  multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#################################################################

def sum_3_5_mult(n: int) -> int:
	'''
	Returns the sum of the multiples of 3 and 5
	up to n.
	input --> int
	output --> int
	'''
	sum_n = 0
	for i in range(n):
		if i % 3 == 0 or i % 5 == 0:
			sum_n += i
	return sum_n


print(sum_3_5_mult(1000))
