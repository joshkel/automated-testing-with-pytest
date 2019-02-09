#!/usr/bin/env python3


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def closed_form_fib(n):
    # Courtesy of Wolfram Alpha
    sqrt_5 = 5 ** 0.5
    phi = (1 + sqrt_5) / 2
    return round(phi ** n / sqrt_5)
