from .helpermodule import log

class Checker():
    def __init__(self, args):
        self.process = args.process
        self.timeInMinutes = args.timeInMinutes

    def run_process(self):
        log(f'Give process :: {self.process}')
        log(f'Give time to check in minutes :: {self.timeInMinutes}')