list = [1, 2, 2, 5, 7, 6, 4, 4, 4, 2, 54, 4, 2, 1, 18]
uniques = []
for number in list:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)
