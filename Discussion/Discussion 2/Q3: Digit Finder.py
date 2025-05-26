def find_digit(k):
    """Returns a function that returns the kth digit of x.
>>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"
    def remove(x):
        num = 0
        # copy_k = k
        while x > 0:
            if k-1 == num:
                return x % 10
            num += 1
            x = x // 10
        return 0
    return remove
    # def inner(x):
    #     count = 0
    #     while x > 0:
    #         if count == k - 1:
    #             return x % 10
    #         x = x // 10
    #         count += 1
    #     return 0
    # return lambda x: (x // pow(10, k - 1)) % 10
print(find_digit(4)(3456))
