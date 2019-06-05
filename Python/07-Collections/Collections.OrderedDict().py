# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
goods = OrderedDict()
for _ in range(int(input())):
    item = input().split()
    item_name, price = ' '.join(item[:-1]), int(item[-1])
    if item_name in list(goods.keys()):
        goods[item_name] += price
    else:
        goods[item_name] = price
for name, net in goods.items():
    print(name, net)
