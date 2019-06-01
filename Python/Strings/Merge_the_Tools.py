def GET_U(TI):
    UI = [''.join([UI_item for index, UI_item in enumerate(TI_item) if UI_item not in TI_item[:index]]) for TI_item in TI]
    for item in UI:
        print(item)

def merge_the_tools(string, k):
    # your code goes here
    split = len(string) // k
    TI = []
    for index in range(split):
        TI.append(string[index * k:(index + 1) * k])
    GET_U(TI)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
