#!/usr/bin/python

'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that
prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples:
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
'''

def brute_force_matching(text, pattern):
    p_len = len(pattern)
    t_len = len(text)

    if p_len > t_len:
        print "pattern cannot exist in text"
        return None

    indexes = []
    for i in range(t_len - p_len + 1):
        substr = text[i:i+p_len]
        found = True
        for j in range(p_len):
            if pattern[j] != text[i+j]:
                found = False
                break

        if found:
            indexes.append(i)

    return indexes

def rabin_karp(text, pattern):
    t_len = len(text)
    p_len = len(pattern)

    if p_len > t_len:
        print "pattern", word, "cannot exist in text", text
        return None

    # Prime number that will be used to generate the hash
    q = 101

    # We will use the ASCII values of the characters
    d = 256

    # Calculate the hash_seed, this will be used later to calculate the rolling hash
    h_seed = 1
    for i in range(p_len - 1):
        h_seed = (h_seed*d)%q

    # Initialize the pattern hash & text hash to 0
    p_hash = 0
    t_hash = 0

    indexes = []

    # Find the hash of the pattern
    for i in range(p_len):
        p_hash = (d*p_hash + ord(pattern[i]))%q
        t_hash = (d*t_hash + ord(text[i]))%q

    # From this point on, we only need to update the rolling hash
    # of the text string
    for i in range(t_len - p_len + 1):
        if t_hash == p_hash and text[i:i+p_len] == pattern:
            indexes.append(i)

        # Roll the window
        if i < t_len - p_len:
            t_hash = (d*(t_hash - ord(text[i])*h_seed) + ord(text[i+p_len]))%q

            if t_hash < 0:
                t_hash = t_hash + q

    return indexes
    

if __name__ == "__main__":
    #indexes = brute_force_matching('aagcgagcgatatatat', 'ata')
    #print "pattern appears at indexes", indexes

    print rabin_karp('aagcgagcgatatatat', 'ata')