if __name__ == '__main__':
    info = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        info.append([name, score])
    info = sorted(info, key=lambda x: x[1])
    second_lowest_grade = sorted(set([i[1] for i in info]))[1]
    names = []
    for member in info:
        if member[1] == second_lowest_grade:
            names.append(member[0])
    for name in sorted(names):
        print(name)

