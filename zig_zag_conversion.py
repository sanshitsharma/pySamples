#!/usr/bin/python

def zigzag(test_str, n_rows):
    i = 0
    j = 0
    k = 0

    print "2D arrays"
    arr = [[None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None], [None, None, None, None, None, None, None]]

    while i < len(test_str):        
        while j < n_rows and i < len(test_str):
            #print "Loop 1: j =", j, " k = ", k, " char: ", test_str[i]
            arr[j][k] = test_str[i]
            j += 1
            i += 1
        
        j -= 2
        k += 1

        while j >= 0 and i < len(test_str):
            #print "Loop 2: j =", j, " k = ", k, " char: ", test_str[i]
            arr[j][k] = test_str[i]
            j -= 1
            k += 1
            i += 1

        j += 2
        k -= 1

    return arr

def main():
    test_str = 'PAYPALISHIRING'
    n_rows = 4

    arr = zigzag(test_str, n_rows)

    rows = len(arr)
    cols = len(arr[0])

    zigzag_str = ''
    for i in range(0, rows):
        for j in range(0, cols):
            if arr[i][j] is not None:
                zigzag_str += arr[i][j]

    print zigzag_str
    
if __name__ == "__main__":
    main()
