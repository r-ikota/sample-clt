import os
dlocation = os.path.dirname(__file__)

f = os.path.join(dlocation, 'data', 'salut.txt')

def pdata():
    with open(f, 'r') as fd:
        for l in fd:
            print(l)

