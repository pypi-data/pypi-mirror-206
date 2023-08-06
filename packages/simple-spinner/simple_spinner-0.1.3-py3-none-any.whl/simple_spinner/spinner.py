"""
reference : https://stackoverflow.com/questions/4995733/how-to-create-a-spinning-command-line-cursor

just practice!!!

"""


import sys
import warnings
import time
import threading
from typing import Optional

class Spinner():
    def __init__(self, desc: Optional[str]="", delay: float=0.5):
        warnings.filterwarnings(action='ignore', category=UserWarning)
        
        self.spinner_generator = self.spinning_cursor()
        self.desc = desc
        self.busy = False
        self.delay = delay
        self.start_time = 0.
        
        if delay and float(delay):
            self.delay = delay
            
    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': 
                yield cursor
                
    def spinner_task(self):
        print(f"[+] {self.desc}...", end=' ')
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()
            
    def __enter__(self):
        self.busy = True
        self.start_time = time.time()
        threading.Thread(target=self.spinner_task).start()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.busy = False
        time.sleep(self.delay)
        
        print(f"end time : {time.time()-self.start_time:.4f}'s")
        if exc_type is not None:
            return False 
        
    def start(self, desc: Optional[str]=""):
        self.busy = True
        self.desc = desc
        self.start_time = time.time()
        threading.Thread(target=self.spinner_task).start()
        
    def stop(self):
        self.busy = False
        time.sleep(self.delay)
        
        print(f"end time : {time.time()-self.start_time:.4f}'s")
        
        
if __name__ == '__main__':
    spinner = Spinner()
    
    spinner.start()
    time.sleep(3)
    spinner.stop()
    
    with Spinner(desc="spinner"):
        time.sleep(3)