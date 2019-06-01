import string
if __name__ == '__main__':
    s = input()

    digit = any(list(map(lambda x: True if x in '0123456789' else False, s)))
    lower = any(list(map(lambda x: True if x in string.ascii_lowercase else False, s)))
    upper = any(list(map(lambda x: True if x in string.ascii_uppercase else False, s)))
    alnum = digit or lower or upper
    alpha = upper or lower
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
