#!/usr/bin/python

'''
Given an encoded string where repetitions of substrings are represented as substring followed by count of substrings.
For example, if encrypted string is "ab2cd2" and k=4 , so output will be "b" because decrypted string is "ababcdcd" and 4th character is "b".

Note: Frequency of encrypted substring can be of more than one digit. For example, in "ab12c3", ab is repeated 12 times
No leading 0 is present in frequency of substring.

Examples:
Input: "a2b2c3", k = 5
Output: c
Decrypted string is "aabbccc"

Input : "ab4c2ed3", k = 9
Output : c
Decrypted string is "ababababccededed"

Input: "ab4c12ed3", k = 21
Output: e
Decrypted string is "ababababccccccccccccededed"
'''

def get_substr_and_reps(string, indx):
    substr = ''
    rep = 0

    while indx < len(string) and string[indx].isalpha():
        substr = substr + string[indx]
        indx = indx + 1

    while indx < len(string) and string[indx].isdigit():
        rep = rep*10 + int(string[indx])
        indx = indx + 1

    return substr, rep, indx

def kth_char_in_decrypted_string(string, k):
    rem_k = k
    indx = 0
    while indx < len(string):
        substr, rep, indx = get_substr_and_reps(string, indx)
        if rep > 0:
            total_chars_parsed = len(substr)*rep
        else:
            total_chars_parsed = len(substr)
        
        if rem_k - total_chars_parsed > 0:
            rem_k = rem_k - total_chars_parsed
            continue
        else:
            if rep > 0:
                substr = substr*rep
            return substr[rem_k - 1]

    return None

if __name__ == "__main__":
    string = 'ab4c12ed3'
    print "21st char in", string, ": ", kth_char_in_decrypted_string(string, 21)

    string = 'ab4c2ed3'
    print "9th char in", string, ": ", kth_char_in_decrypted_string(string, 9)

    string = 'a2b2c3'
    print "4th char in", string, ": ", kth_char_in_decrypted_string(string, 4)

    string = 'aabbccc'
    print "2nd char in", string, ": ", kth_char_in_decrypted_string(string, 2)