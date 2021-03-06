import argparse, sys
from .checker import Checker
from .helpermodule import check_positive

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('-p', '--process', help='Enter the process name')
    parser.add_argument('-t', '--timeInSeconds', help='Enter the time to check in seconds', type=check_positive)
    parser.add_argument('-s', '--script', help='Enter the shell script path', default='')
    args=parser.parse_args()
    if not args.process:
        parser.error('Please specify the process name with -p or --process option')
    if not args.timeInSeconds:
        parser.error('Please specify the time to check in seconds with -t or --timeInSeconds')
    if not args.script:
        args.script = args.process
    checker = Checker(args)
    checker.runprocess()

if __name__ == '__main__':
    main()