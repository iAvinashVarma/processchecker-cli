import argparse, sys

def log(text_to_display):
    print('{}'.format(text_to_display))

def check_positive(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive numeric value" % value)
        return ivalue
    except:
        raise argparse.ArgumentTypeError("%s is an invalid numeric value" % value)
    