# There are two-ways to get the sum of first n natural numbers.
# 1. Parameterised way
# 2. Functional Recusrsion way
# 3. Formula way: sum = n*(n+1)/2

# Functional Recursion way

def FuncRec(n):
        #When Base condition is called, then recursion will occur
        if n == 0:
            return 0
        return n + FuncRec(n - 1)
    
n = 4
print("Sum is:", FuncRec(4))
        