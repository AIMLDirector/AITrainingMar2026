import argparse
import sys

parser = argparse.ArgumentParser(description='Testing the argument parser')

parser.add_argument('--dir',  help='Enter the directory name as input', required=True)
parser.add_argument('--name',  help='Enter your name as input', type=str, required=True)
args = parser.parse_args()

if args.dir and args.name:
    print("Directory path provided:", args.dir, "and name provided:", args.name)
else:
    print("Please provide a directory path  and name as a command-line argument.")
    sys.exit(1)