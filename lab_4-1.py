# Kyle Bautista (AMDG) 2/4/2021

grades = {'Cycle 10 Labs': 80, 'HW 10-1': 75, 'HW 10-2': 20, 'HW 10-3': 90, 'HW 10-4': 100}

scores = list(grades.values())
print(scores)

for name in grades:
    print(name)

for k, v in grades.items():
    if v >= 80:
        print("{0}, {1}".format(k, v))
