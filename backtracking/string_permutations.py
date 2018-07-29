#!/usr/bin/python
'''
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

'''

def permute(l, indx):
    if indx == len(l)-1:
            print ''.join(l)
            return

    for j in range(indx, len(l)):
            l[indx], l[j] = l[j], l[indx]
            permute(l, indx+1)
            l[indx], l[j] = l[j], l[indx]

def main():
    string = 'JON'
    lst = list(string)
    start = 0
    end = len(string) - 1
    permute(lst, start)
    #Permutations.permutations(string)

if __name__ == "__main__":
    main()
