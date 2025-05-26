# def is_prime(n):
#     assert n > 1
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def f(i):
        if n // i == 0:
            return False
        elif n // i == 1:
            return True
        else:
            return f(i + 1)
    return f(2)
