import en_local as en

from sympy import *


p, q = symbols('p q')

Qd = 794 - 150 * p

N = int(input(en.FIRM_K_INPUT))
print(en.FIRMS_EXEMPT_NUM, 0.2 * N)

print(en.FIRMS_NOT_EXEMPT_NUM, N - 0.2 * N)

# consider a tax-exempt company:

TC = 0.1 * q ** 2 + 2  # Total costs

MC = diff(TC, q)  # Marginal costs

print(en.FIRM_OFFER_MC, solve(MC - p, p))

q1 = solve(MC - p, q)

print('MC = p, q1 =', solve(MC - p, q))

# consider a company that pays tax

TCn = 0.1 * q ** 2 + 2 + 1.6 * q

MCn = diff(TCn, q)

q2 = solve(MCn - p, q)

print(en.FIRM_OFFER_MC, solve(MCn - p, p))

print('MCn = p, q2 =', solve(MCn - p, q))

Qs = 8 * 5 * p + 32 * (5 * p - 8)

print(en.OFFER_IN_BRANCH, solve(8 * 5 * p + 32 * (5 * p - 8), p))

print('Qd = Qs, po =', solve(Qd - Qs, p))

q11 = 5 * 3

q22 = 5 * 3 - 8

print(en.PRODUCT_TAXED, 32 * q22)

print(en.TAX_REVENUES, round((1.6 * 32 * q22), 2))
