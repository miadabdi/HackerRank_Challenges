import re

def wrapper(func):
    def fun(phoneList):
        # complete the function
        regex = r'^(\+91|91|0)?(\d{5})(\d{5})$'
        items = [re.findall(regex, elem)[0] for elem in phoneList]
        new_phones = map(lambda x: '{} {} {}'.format('+91', x[1], x[2]) , items)
        func(list(new_phones))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


