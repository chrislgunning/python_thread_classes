import pexpect
import threading
import time

class StoppableCmdThread(threading.Thread):

    def __init__(self, target_command, *args, **kwargs):
        super(StoppableCmdThread, self).__init__(*args, **kwargs)
        self.target_command  =  target_command
        self.process = None
    
    def run(self):
        print('Spawning process.\n');
        self.process = pexpect.spawn('/bin/bash',  ['-c',  self.target_command])
        while(self.process.isalive()):
            time.sleep(1)

    def stop(self):
        if self.process != None:
            while (self.process.isalive()):
                self.process.sendcontrol('c')
                print('Stopping process.\n');
                time.sleep(2)
                
    def readline(self):
        line = None
        if self.process != None:            
            line = self.process.readline()
        return line
