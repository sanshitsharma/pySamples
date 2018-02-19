#!/usr/bin/python

class Permutations:
    @staticmethod
    def permutations(test_str):
        a = list(test_str)
        Permutations().permute(a, 0)
    
    def __toString(self, List):
        return ''.join(List)

    def permute(self, a, l):
        if l==len(a)-1:
            print self.__toString(a)
        else:
            for i in xrange(l,len(a)):
                a[l], a[i] = a[i], a[l]
                self.permute(a, l+1)
                a[l], a[i] = a[i], a[l] # backtrack

def permute(lst, start, end):
    if start == end:
        print ''.join(lst)
        return

    for i in range(start, end+1):
        lst[start], lst[i] = lst[i], lst[start]
        permute(lst, start+1, end)
        lst[start], lst[i] = lst[i], lst[start]

def main():
    string = 'JON'
    lst = list(string)
    start = 0
    end = len(string) - 1
    permute(lst, start, end)
    #Permutations.permutations(str)

if __name__ == "__main__":
    main()
