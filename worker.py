import hashlib
import boto
from task import Task

class Worker(object):

    def __init__(self, task):
        self.task = task

    def start(self):
        # check wheather the task is existed
        if task.is_dup:
            return

        m = hashlib.sha1()

        #TODO: start downloading

        # after
        self.checksum = m.hexdigest()
        self.task.finish(self.checksum)
        self.save_to_s3()

    def save_to_s3(self):
        #TODO
        pass

if __name__ == '__main__':
    while(True):
        #TODO: read message from sqs
        url = ''
        task = Task(url)
        worker = Worker(task)
        worker.start()