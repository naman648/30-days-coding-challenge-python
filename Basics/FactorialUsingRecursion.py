def Factorial(n):
    if n==1:
        return 1
    return n * Factorial(n-1)   ## (n-1) for going back like 9..8..7..6..5..4..etc.
# Example usage
n = 4
print (Factorial(n))