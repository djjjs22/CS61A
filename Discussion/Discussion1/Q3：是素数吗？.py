def is_prime(n):
    i = 2
    while i < n:
        if i % n ==0:
            return False
        i = i + 1
    return True
print(is_prime(13))
