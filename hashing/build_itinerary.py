#!/usr/bin/python

'''
Given a list of tickets, find itinerary in order using the given list.

Example:

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
It may be assumed that the input list of tickets is not cyclic and there is one ticket from every city except final destination.
'''

def build_itinerary(tickets):
    countMap = {}
    src_dst = {}

    # Build the maps
    for ticket in tickets:
        # Add the ticket
        src_dst[ticket[0]] = ticket[1]

        # Add the city count to countMap
        try:
            countMap[ticket[0]] += 1
        except:
            countMap[ticket[0]] = 1

        try:
            countMap[ticket[1]] += 1
        except:
            countMap[ticket[1]] = 1

    # Find the originating city
    for k, v in countMap.items():
        if v == 1 and k in src_dst.keys():
            oCity = k

    # Build the itinerary
    itinerary = []
    while oCity in src_dst.keys():
        itinerary.append((oCity, src_dst[oCity]))
        oCity = src_dst[oCity]

    return itinerary


if __name__ == "__main__":
    print build_itinerary([('Chennai', 'Bangalore'), ('Bombay', 'Delhi'), ('Goa', 'Chennai'), ('Delhi', 'Goa')])