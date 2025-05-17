def prime(n):
    if n <= 1:
        return "Not a prime"
    for i in range (2,n):
        if n%i == 0:
            return "Not a prime"
    return "Prime"
# Example usage:
print(prime(61))