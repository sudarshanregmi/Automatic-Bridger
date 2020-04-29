import argparse
from config import credentials as cred


parser = argparse.ArgumentParser()
parser.add_argument('--v', default='0', type=str, help='Specify type of link')
args = parser.parse_args()


if args.v=='0':
    url = f"http://{cred['USERNAME']}:{cred['PASSWORD']}@192.168.0.1/"
else:
    url = f"http://{cred['USERNAME']}:{cred['PASSWORD']}@192.168.1.1/"

