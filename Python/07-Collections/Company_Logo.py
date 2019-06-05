import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    Counts = Counter(s)
    Counts = sorted(Counts.items(), key=lambda x:(-x[1], x[0]))
    [print(item[0], item[1]) for item in Counts[:3]]

