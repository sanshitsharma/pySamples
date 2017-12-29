#!/usr/bin/python

from collections import OrderedDict 

def roman_to_integer(r_num):
    d = OrderedDict()
    d['I'] = 1
    d['V'] = 5
    d['X'] = 10
    d['L'] = 50
    d['C'] = 100
    d['D'] = 500
    d['M'] = 1000
    r_num = r_num.upper()

    num = 0
    indx = 0
    while indx < len(r_num):
        if indx + 1 < len(r_num) and d.keys().index(r_num[indx+1]) > d.keys().index(r_num[indx]):
            num = num + (d[r_num[indx+1]] - d[r_num[indx]])
            indx += 2
        else:
            num = num + d[r_num[indx]]
            indx += 1

    return num

def main():
    print "Given a roman numeral convert it to integer. Input is guranteed to be between 1 & 3999"

    roman = 'DCXXI'
    print "'" + roman + "' --> " + str(roman_to_integer(roman))

if __name__ == "__main__":
    main()