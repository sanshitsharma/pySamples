#!/usr/bin/env python

'''
388. Longest Absolute File Path

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

Ref: https://leetcode.com/problems/longest-absolute-file-path/description/
'''

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longest_file_path_length = 0
        stk = []
        dirs = input.split('\n')

        for i in range(len(dirs)):
            file = dirs[i]
            fileName = file.strip('\t')
            fileDepth = file.count('\t')

            print "Processing name =", fileName, "depth:", fileDepth, "stk:", stk

            if not stk or fileDepth > stk[-1][1]: # stk[-1][1] ==> depth of top element in the stack
                stk.append((fileName, fileDepth))
            elif fileDepth < stk[-1][1]:
                while fileDepth < stk[-1][1]:
                    if self.isFile(stk[-1][0]) and longest_file_path_length < self.getPathLength(stk):
                        longest_file_path_length = self.getPathLength(stk)
                    stk.pop()
                # Replace the top element
                stk.pop()
                stk.append((fileName, fileDepth))
            else: # fileDepth == stk[-1][1]
                while fileDepth == stk[-1][1]:
                    if self.isFile(stk[-1][0]) and longest_file_path_length < self.getPathLength(stk):
                        longest_file_path_length = self.getPathLength(stk)
                    stk.pop()
                # Finally add the new element on top
                stk.append((fileName, fileDepth))

        return max(longest_file_path_length, self.getPathLength(stk))
                    
    def getPathLength(self, stk):
        path = ''
        for elem in stk:
            path += elem[0] + '/'
        
        return len(path[:-1])

    def isFile(self, name):
        try:
            name.index('.')
            return True
        except:
            return False

if __name__ == "__main__":
    #ip = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    ip = 'dir\n\tfile.txt'
    print Solution().lengthLongestPath(ip)