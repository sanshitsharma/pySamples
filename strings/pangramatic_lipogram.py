#!/usr/bin/python

'''
Check if a string is Pangrammatic Lipogram
To understand what a pangrammatic lipogram is we will break this term down into 2 terms i.e. a pangram and a lipogram

Pangram: A pangram or holoalphabetic sentence is a sentence using every letter of a given alphabet at least once.
The best-known English pangram is "The quick brown fox jumps over the lazy dog."

Lipogram: A lipogram is a kind of constrained writing or word game consisting of writing paragraphs or longer works in 
which a particular letter or group of letters is avoided-usually a common vowel, and frequently E, the most common letter 
in the English language.

Example: The original "Mary Had a Little Lamb" was changed by A. Ross Eckler Jr. to exclude the letter 'S'.
Original:
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go

Lipogram (Without "S"):
Mary had a little lamb
With fleece a pale white hue
And everywhere that Mary went
The lamb kept her in view

Pangrammatic Lipogram:
A pangrammatic lipogram is a text that uses every letter of the alphabet except one. For example,
"The quick brown fox jumped over the lazy dog" omits the letter S, which the usual pangram includes by using the word jumps.

Given a string, our task is to check whether this string is a pangrammatic lipogram or not?

Sample: 
Input: ["The quick brown fox jumped over the lazy dog", "The quick brown fox jumps over the lazy dog", "The quick brown fox jum over the lazy dog"]
Output:
    Pangrammatic Lipogram
    Pangram
    Not a Pangram but might a Lipogram
'''
import math
#from datetime import datetime

def panLipogramChecker(s):
    allAlphabets = pow(2,26)-1
    alphabets = 0

    for char in s:
        if char == ' ':
            continue
        char = char.lower()
        charIndex = ord(char) - ord('a')
        alphabets = alphabets | 1 << charIndex

    if alphabets == pow(2,26)-1:
        return 'Pangram'
    elif math.log((alphabets ^ allAlphabets), 2).is_integer():
        return 'Pangrammatic Lipogram'
    else:
        return 'Not a Pangram but might a Lipogram'

if __name__ == "__main__":
    strs = ["The quick brown fox jumped over the lazy dog", "The quick brown fox jumps over the lazy dog", "The quick brown fox jum over the lazy dog"]
    for s in strs:
        #start_time = datetime.now()
        print panLipogramChecker(s)
        #print("--- %s microseconds ---" % (datetime.now() - start_time).microseconds)