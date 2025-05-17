def AllDivisors(n):
    # Base case:
    if n == 1:
        return 1
    else:
        div = []
        for i in range(1,n):
            if n%i == 0:
                div.append(i)
        return div
                 
# Example usage:
print(AllDivisors(1))
