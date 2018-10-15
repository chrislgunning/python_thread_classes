import os
import threading
import time

class ExternalProcessThread(threading.Thread):
    
    
    def __init__(self,  process_name,  command,  *args, **kwargs):
        super(ExternalProcessThread, self).__init__(*args, **kwargs)
        self.process_name = process_name
        self.command = command
        self.kill_command = 'killall -9 {0}'.format(self.process_name)

    def run(self):
        os.system(self.command)
        time.sleep(2)
        while(self.is_running()):
            time.sleep(1)

    def is_running(self):
        running_processes = os.popen('ps -Af').read()
        is_running = self.process_name in running_processes
        return is_running
    
    def stop(self):
        os.system(self.kill_command)

