import threading
import time

class WorkerThread(threading.Thread):

    def __init__(self):
        super(WorkerThread, self).__init__()
        self.stoprequest = threading.Event()

    def run(self):
        while not self.stoprequest.isSet():
            print("working on")
            time.sleep(1)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(WorkerThread, self).join(timeout)
        print("end working")
