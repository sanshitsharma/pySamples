#!/usr/bin/env python

def get_hex_value(n):
    if n < 0 or n > 15:
        raise ValueError(n, "does not have a hex representation")

    if n >= 0 and n <= 9:
        return str(unichr(n + 48))

    return str(unichr(n + 55))

def convert_to_hex(num, res):
    if num == 0:
        res = ['0', 'x'] + res
        return ''.join(res)

    res = [get_hex_value(num%16)] + res
    return convert_to_hex(num/16, res)

if __name__ == "__main__":
    res = []
    hex = convert_to_hex(239, res)
    print hex