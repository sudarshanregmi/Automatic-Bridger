import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--v', default='0', type=str, help='Specify type of link')
args = parser.parse_args()


if args.v=='0':
    url = 'http://admin:admin@192.168.0.1/'
else:
    url = 'http://admin:admin@192.168.1.1/'

