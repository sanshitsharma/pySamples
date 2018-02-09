#!/usr/bin/python

def solve(grades):
    fGrades = []
    for grade in grades:
        if grade < 38 or grade%5 == 0:
            fGrades.append(grade)
            continue

        quo = grade/5
        if ((quo+1)*5 - grade) < 3:
            fGrades.append((quo+1)*5)
        else:
            fGrades.append(grade)
    
    return fGrades
if __name__ == "__main__":
    print solve([73, 67, 38, 33])
