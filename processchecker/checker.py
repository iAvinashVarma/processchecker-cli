import time, psutil, sys, os
from .helpermodule import logInfo

class Checker():
    def __init__(self, args):
        self.process = args.process
        self.timeInSeconds = args.timeInSeconds

    def runprocess(self):
        logInfo(f'Given process :: {self.process}')
        logInfo(f'Given time to check in seconds :: {self.timeInSeconds}')
        while True:
            try:
                logInfo(f'Check if process :: {self.process} is running.')
                if self.__isprocessrunning():
                    logInfo(f'Yes a {self.process} process was already running')
                else:
                    logInfo(f'No {self.process} process was not running, need to run')
                    self.__startprocess()
                time.sleep(self.timeInSeconds)
            except KeyboardInterrupt:
                logInfo("Bye")
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
        logInfo(f'Running {self.process} process...')
        os.system(f'{self.process}')