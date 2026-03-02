import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    if y > 1:
        y = y / 100.0
    if couponRate > 1:
        couponRate = couponRate / 100.0

    n = int(m * ppy)
    t = np.arange(1, n + 1)

    c = face * couponRate / ppy
    r = y / ppy

    cashflows = np.full(n, c, dtype=float)
    cashflows[-1] += face

    pv = cashflows / ((1.0 + r) ** t)
    times = t / ppy 

    duration = np.sum(times * pv) / np.sum(pv)

    return float(np.round(duration, 2))
