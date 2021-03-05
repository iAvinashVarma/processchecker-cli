import argparse, sys
from .checker import Checker
from .helpermodule import check_positive

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p', '--process', help='Enter the process name')
    parser.add_argument('-t', '--timeInMinutes', help='Enter the time to check in minutes', type=check_positive)
    args=parser.parse_args()
    if not args.process:
        parser.error('Please specify the process name with -p or --process option')
    if not args.timeInMinutes:
        parser.error('Please specify the time to check in minutes with -t or --timeInMinutes')
    checker = Checker(args)
    checker.run_process()

if __name__ == '__main__':
    main()