def mean(numbers):
    meangin = float(sum(numbers)) / max(len(numbers), 1)
    number_dec = str(meangin - int(meangin))[2:]
    if len(number_dec) < 2:
        return str(int(meangin)) + '.' + number_dec + '0'
    if len(number_dec) > 2:
        return str(int(meangin)) + '.' + number_dec[:2]
    else:
        return str(meangin)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(mean(student_marks[query_name]))
