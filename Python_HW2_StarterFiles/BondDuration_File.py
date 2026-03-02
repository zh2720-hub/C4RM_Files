import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    r = y / ppy

    cashflows = np.full(n, coupon, dtype=float)
    cashflows[-1] += face

    pv_cashflows = cashflows / ((1 + r) ** t)
    times = t / ppy

    duration = np.sum(times * pv_cashflows) / np.sum(pv_cashflows)

    return float(np.round(duration, 2))
