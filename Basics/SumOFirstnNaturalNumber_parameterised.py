# There are two-ways to get the sum of first n natural numbers.
# 1. Parameterised way
# 2. Functional Recusrsion way

# PARAMETERISED WAY

class Solution:
    def SumOfN(n):
        # Base
        if n<1:
            return 0

        sum = 0
        for i in range(1,n+1):
             sum = i + sum
        return sum
    
    result = SumOfN(5)
    print("The Sum is: ",result)


