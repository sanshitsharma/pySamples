#!/usr/bin/env python

def get_dec_and_frac(num):
    if isinstance(num, int):
        return num, 0
    elif isinstance(num, float):
        return int(str(num)[:str(num).index('.')]), float(str(num)[str(num).index('.'):])
    else:
        raise ValueError('invalid type')

def convert(num, precision=8):
    is_neg = False
    if num < 0:
        is_neg = True
        num = abs(num)

    try:
        d, f = get_dec_and_frac(num)
    except ValueError as ve:
        print ve
        return None

    d_bin = ''
    while d != 0:
        d_bin = str(d%2) + d_bin
        d = d/2

    f_bin = ''
    p_count = 0
    while f != 0 and p_count < precision:
        quo, f = get_dec_and_frac(f*2)        
        f_bin += str(quo)
        p_count += 1

    if is_neg:
        prefix = "b'1"
    else:
        prefix = "b'0"

    if f_bin == '':
        return prefix + d_bin + "'"
    
    return prefix + d_bin + "." + f_bin + "'"

if __name__ == "__main__":
    num = -9.12
    res = convert(num, 32)
    print "Binary notation of num:", res