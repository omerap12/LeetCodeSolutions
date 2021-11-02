class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = ""
        for i in range(len(y)-1,-1,-1):
            z += y[i]
        print(z)
        return z == y
