results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9,
           12.9, 37.4]
allResultOver10 = [x for x in results if str(x).startswith("10")]
threeBestResult = sorted(results)[-3:]
threeWorseResult = sorted(results)[:3]

print("3Best: ", threeBestResult)
print("3Worse: ", threeWorseResult)
print("Результаты начинающиеся с 10 =", allResultOver10)
