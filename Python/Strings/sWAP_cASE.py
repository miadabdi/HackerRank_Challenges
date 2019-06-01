def letters(letter):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in lower:
        return letter.upper()
    elif letter in upper:
        return letter.lower()
    else:
        return letter

def swap_case(s):
    return ''.join(list(map(letters, s)))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

