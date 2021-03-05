import time, psutil, sys, os
from .helpermodule import log

class Checker():
    def __init__(self, args):
        self.process = args.process
        self.timeInSeconds = args.timeInSeconds

    def runprocess(self):
        log(f'Given process :: {self.process}')
        log(f'Given time to check in seconds :: {self.timeInSeconds}')
        while True:
            try:
                log(f'Check if process :: {self.process} is running.')
                if self.__isprocessrunning():
                    log(f'Yes a {self.process} process was already running')
                else:
                    log(f'No {self.process} process was not running, need to run')
                    self.__startprocess()
                time.sleep(self.timeInSeconds)
            except KeyboardInterrupt:
                log("Bye")
                sys.exit()
        
    def __isprocessrunning(self):
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if self.process.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def __startprocess(self):
        os.system(f'{self.process}')