from string import ascii_letters, digits
def fun(s):
    # return True if s is a valid email, else return False
    if s.count('.') == 1 and s.count('@') == 1:
        s, extension = s.split(".")
        username, domain = s.split("@")
        if len(extension) < 4 and len(extension) > 0:
            expression = lambda x: True if x in ascii_letters or x in digits else False
            if all(list(map(expression, domain))) and len(domain) > 0:
                expression = lambda x: True if x in ascii_letters or x in digits or x in '_-' else False
                if all(list(map(expression, username))) and len(username) > 0:
                    return True
    return False    


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
