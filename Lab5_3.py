one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]


def getTriangleArea(a, b, c):
    return (a * b * c) / 2;


minOne = min(one);
maxOne = max(one);
minTwo = min(two);
maxTwo = max(two);
minThree = min(three);
maxThree = max(three);

print(getTriangleArea(minOne, minTwo, minThree));
print(getTriangleArea(maxOne, maxTwo, maxThree));
