import xml.etree.ElementTree as etree

def depth2(elem):
    if len(list(elem)):
        if not any([list(item) for item in list(elem)]):
            return 1
        else:
            return 1 + max([depth2(item) for item in list(elem)])
    else: return 0

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    maxdepth = depth2(elem)
    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)