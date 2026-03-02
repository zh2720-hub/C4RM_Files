import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    r = y / ppy

    cashflows = np.full(n, coupon, dtype=float)
    cashflows[-1] += face

    discount_factors = (1 + r) ** t
    price = np.sum(cashflows / discount_factors)

    return price
