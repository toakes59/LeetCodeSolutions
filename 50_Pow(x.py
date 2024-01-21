# Pow(x
# Define a function named 'myPow' that takes two parameters 'x' (base) and 'n' (exponent).
def myPow(x, n):
    # Base case: if the exponent 'n' is 0, return 1.0 (any number raised to the power of 0 is 1).
    if n == 0:
        return 1.0
    
    # If the exponent 'n' is negative, adjust the base 'x' and exponent 'n'.
    if n < 0:
        x = 1 / x
        n = -n

    # Recursively calculate the power of 'x' to the power of 'n // 2'.
    half_pow = myPow(x, n // 2)

    # If 'n' is even, return the square of the result of the recursive call.
    if n % 2 == 0:
        return half_pow * half_pow
    # If 'n' is odd, return the square of the result multiplied by 'x'.
    else:
        return half_pow * half_pow * x


# Example usage:
x = 2.0
n = 10
result = myPow(x, n)
print(result)
