import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name', help="greeting you with this name")

def salut():
    args = parser.parse_args()
    print('Hello, {0:s}'.format(args.name))