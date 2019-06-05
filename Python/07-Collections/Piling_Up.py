# Enter your code here. Read input from STDIN. Print output to STDOUT
def possibility(cubes):
    copied_cubes = cubes.copy()
    vertical_pile = []
    while len(cubes):
        if cubes[0] > cubes[-1]:
            vertical_pile.append(cubes.pop(0))
        elif cubes[0] <= cubes[-1]:
            vertical_pile.append(cubes.pop())
    if vertical_pile == sorted(copied_cubes, reverse = True):
        print("Yes")
    else:
        print("No")

for _ in range(int(input())):
    n = int(input())
    cubes = list(map(int, input().split()))
    possibility(cubes)
