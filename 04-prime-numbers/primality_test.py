#!/usr/bin/env python3

from random import randrange

def miller_rabin(n, k=4):
    """
    Probabilistic test to determine if a number is prime or not. It is based on 
    Fermat's little theorem (a^p ≡ a (mod p)).

    Args:
        n: The number to be checked if is prime or not.
        k: The number of tests to determine if 'n' is prime.

    Returns:
        False means "composite", true means "possible prime".
    """
    assert n >= 2
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = n-1
    s = 0
    while d % 2 != 0:
        d = d >> 1
        s += 1

    for _ in range(k):
        a = randrange(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                continue
        return False
    return True


def fermat(n, k=4):
    """
    Simplest probabilistic test to determine if a number is prime. It verifies
    the number composition through modular exponentiation.

    Args:
        n: The number to be checked if is prime or not.
        k: The number of tests to determine if 'n' is prime.

    Returns:
        False means "composite", true means "possible prime".
    """
    assert n > 4

    for _ in range(k):
        a = randrange(2, n-2)
        if pow(a, n-1, n) != 1:
            return False
    return True
