import math

def getTriangleSquare(a, b, c):
    p = (a + b + c) / 2
    s = float('%.6f' % math.sqrt(p * (p - a) * (p - b) * (p - c)))
    return (s)
