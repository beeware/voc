import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='Getting foo help')
args = parser.print_help()
