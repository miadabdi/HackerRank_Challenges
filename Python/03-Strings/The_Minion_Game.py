__Auther__ = 'Anatoli Babenia'  # https://www.hackerrank.com/abitrolly

def minion_game(string):
    # your code goes here
    StuartsScore = 0
    KevinsScore = 0
    vowels = 'AEIOU'
    for index in range(len(string)):
        if string[index] in vowels:
            KevinsScore += len(string) - index
        else:
            StuartsScore += len(string) - index

    if StuartsScore > KevinsScore:
        print("Stuart {}".format(StuartsScore))
    elif StuartsScore < KevinsScore:
        print("Kevin {}".format(KevinsScore))
    elif StuartsScore == KevinsScore:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
