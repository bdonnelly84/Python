""" These are the functions developed in the Practice Makes Perfect Module @ Codecademy """
""" Exercises completed thus far: 2/15; 3/15; 4/15; 6/15; 8/15; 10/15; 11/15; 12/15; 13/15; 14/15; 15/15 """

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
def censor(text,word):
    text_list = text.split()
    result_list = []
    result_string = ""
    length = len(word)
    for a in text_list:
        if a == word:
            result_list.append("*"*length)
        else:
            result_list.append(a)
    result_string = ' '.join(str(e) for e in result_list)
    return result_string

""" Exercise 11/15 """
def count(sequence,item):
    count = 0
    index = 0
    for s in sequence:
        if sequence[index] == item:
            count += 1
            index += 1
        else:
            index += 1
    return count

""" Exercise 12/15 """
def purify(x):
    result = []
    for a in x:
        if a % 2 == 0:
            result.append(a)
        else:
            continue
    return result

""" Exercise 13/15 """
def product(x):
    product = 1
    for number in x:
        product = product * number
    return product

""" Exercise 14/15 """
def remove_duplicates(numbers):
    result = []
    for a in numbers:
        if a not in result:
            result.append(a)
    return list

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
