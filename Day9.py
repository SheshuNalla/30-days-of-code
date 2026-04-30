def fact(n):
    if n==0:
        return 1
    return n * fact(n-1) # Recursion is a programming technique where a function calls itself to solve a problem.


ans = fact(4)
print(ans)