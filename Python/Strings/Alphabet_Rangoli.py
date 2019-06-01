import string
def print_rangoli(size):
    # your code goes here
    alpha = list(string.ascii_lowercase)
    start = size
    for _ in range(size * 2 - 1):
        if _ < (size * 2 - 1) // 2:
            strin = '-'.join(alpha[start:size])[::-1] + '-' + '-'.join(alpha[start - 1:size])
            if _ == 0:
                strin = strin[-1]
            print(strin.center((size * 2 - 1) * 2 -1, '-'))
            start -= 1
        elif _ == (size * 2 - 1) // 2:
            strin = '-'.join(alpha[start:size])[::-1] + '-' + '-'.join(alpha[start - 1:size])
            if size == 1:
                strin = strin[-1]
            print(strin.center((size * 2 - 1) * 2 -1, '-'))
        elif _ > (size * 2 - 1) // 2:
            start += 1
            strin = '-'.join(alpha[start:size])[::-1] + '-' + '-'.join(alpha[start - 1:size])
            if _ == size * 2 - 1 - 1:
                strin = strin[-1]
            print(strin.center((size * 2 - 1) * 2 -1, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
