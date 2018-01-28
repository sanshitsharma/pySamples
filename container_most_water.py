#!/usr/bin/python

def most_water(a):
    max_area = left = right = 0
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            width = j - i
            height = min(a[i], a[j])
            area = width * height

            if area > max_area:
                max_area = area
                left = i
                right = j

    return max_area, left, right

def max_water(a):
    area = 0
    l = 0
    r = len(a) - 1
    
    while l < r:
        area = max(area, min(a[l], a[r]) * (r-l))

        if (a[l] < a[r]):
            l += 1
        else:
            r -= 1

    return area

def main():
    print "Find two lines, which together with x-axis forms a container, such that the container contains the most water."
    a = [3, 1, 2, 4, 5]

    area, left_indx, right_indx = most_water(a)
    print "Container with most water is between '" + str(a[left_indx]) + "' & '" + str(a[right_indx]) + "' with an area of '" + str(area) + "'"

    print "Max Area: " + str(max_water(a))

if __name__ == "__main__":
    main()