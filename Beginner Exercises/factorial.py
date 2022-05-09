# Factorial: a very common beginner exercise

# Solution 1 (recursion)
def fac_rec(n):
    if n == 1:
        return 1
    else:
        return n * fac_rec(n - 1)


# Solution 2 (iteration)
def fac_ite(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


# Test the two solutions
print(fac_rec(5))
print(fac_ite(5))
