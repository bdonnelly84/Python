""" These are the functions developed in the Practice Makes Perfect Module @ Codecademy """
""" Exercises completed thus far: 2/15; 3/15; 4/15; 6/15; 8/15; 13/15; 15/15 """

""" Exercise 2/15 """
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

""" Exercise 3/15 """
def is_int(x):
    if type(x) is int:
        return True
    elif float(x) - int(x) == float(0):
        return True
    else:
        return False

""" Exercise 4/15 """
def digit_sum(n):
    total = 0
    n1 = str(n)
    for i in n1:
        total = total + int(i)
    return total

""" Exercise 5/15 """

""" Exercise 6/15 """
def is_prime(x):
    start = 2
    if x < 2:
        return False
    else:
        while start <= (x-1) and x >= 2:
            if x % start == 0 and start <= (x-1):
                return False
            start = start + 1
        return True

""" Exercise 7/15 """

""" Exercise 8/15 """
def anti_vowel(text):
    t = ""
    for c in text:
        if c not in "aeiouAEIOU":
            t += c
    return t

""" Exercise 9/15 """

""" Exercise 10/15 """

""" Exercise 11/15 """

""" Exercise 12/15 """

""" Exercise 13/15 """
def product(x):
    product = 1
    for number in x:
        product = product * number
    return product

""" Exercise 14/15 """

""" Exercise 15/15 """
def median(x):
    sort = sorted(x)
    if len(sort) % 2 != 0:
        a = len(sort) - ((len(sort)-1)/2)
        return sort[(a-1)]
    else:
        b = (len(sort))/2
        c = b + 1
        d = (sort[(b-1)]+sort[(c-1)])
        e = float(d)
        f = e/2
        return f
