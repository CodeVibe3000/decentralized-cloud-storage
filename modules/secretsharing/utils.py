import random
from math import ceil
from decimal import Decimal

FIELD_SIZE = 10**5


def reconstruct_secret(shares):
	sums = 0
	prod_arr = []

	for j, share_j in enumerate(shares):
		xj, yj = share_j
		prod = Decimal(1)

		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				prod *= Decimal(Decimal(xi)/(xi-xj))

		prod *= yj
		sums += Decimal(prod)

	return int(round(Decimal(sums), 0))


def polynom(x, coefficients):
	point = 0

	for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
		point += x ** coefficient_index * coefficient_value
	return point


def coeff(t, secret):
	coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t - 1)]
	coeff.append(secret)
	return coeff


def generate_shares(n, m, secret):
	coefficients = coeff(m, secret)
	shares = []

	numbers = random.sample(range(1, FIELD_SIZE), n)

	shares = [(x, polynom(x, coefficients)) for x in numbers]

	return shares