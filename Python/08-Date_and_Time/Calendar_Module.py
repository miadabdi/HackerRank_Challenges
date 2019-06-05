# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import weekday, day_name
month, day, year = list(map(int, input().split()))
print(day_name[weekday(year, month, day)].upper())
