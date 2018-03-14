#!/usr/bin/python

def convert_dec_to_binary(num):
    lst = []
    while num != 0:
        lst.append(str(num%2))
        num = num/2

    lst.reverse()
    return "".join(lst)

def are_binary_anagrams(num1, num2):
    # We only need to count 1 bits
    count = 0
    while num1 != 0:
        if num1 & 1 == 1:
            count = count + 1
        num1 = num1 >> 1

    while num2 != 0:
        if num2 & 1 == 1:
            count = count - 1
        num2 = num2 >> 1

    return count == 0

if __name__ == "__main__":
    num1 = 9
    num2 = 3
    if are_binary_anagrams(num1, num2):
        print num1, "&", num2, "are binary anagrams"
    else:
        print num1, "&", num2, "are NOT binary anagrams"