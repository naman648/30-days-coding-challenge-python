# There are two ways to count the digits:
# 1. By converting int to str
# 2. By initialising count=0 and counting +1

# First-method

def countDigit(n):
    # Base case
    if n == 0 :
        return 1
    # Conversion
    digit = str(n)
    count = len(digit)
    print(count)

# Example usage:
n = 12345
countDigit(n)