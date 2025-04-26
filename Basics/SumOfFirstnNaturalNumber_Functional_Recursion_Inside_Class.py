# There are two-ways to get the sum of first n natural numbers.
# 1. Parameterised way
# 2. Functional Recusrsion way
# 3. Formula way: sum = n*(n+1)/2

# Functional Recursion way

class Solution:
    def FuncRec(self, n):
            #When Base condition is called, then recursion will occur
            if n == 0:
                return 0
            return n + self.FuncRec(n - 1)
        
sol = Solution()
print("Sum is:", sol.FuncRec(4))