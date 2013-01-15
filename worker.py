import hashlib
import boto
from task import Task
from urllib2 import urlopen
import os
import tempfile
import time

class Worker(object):

    def __init__(self, task):
        self.task = task

    def start(self):
        m = hashlib.sha1()

        f = urlopen(url)
        BLOCKSIZE = 4 * 1024 * 1024

        self.temp = tempfile.TemporaryFile()
        while True:
            data = f.read(BLOCKSIZE)
            if not data:
                break
            self.temp.write(data)
            m.update(data)

        # after
        self.checksum = m.hexdigest()
        self.task.finish(self.checksum, os.path.basename(url))
        self.save_to_s3()

    def save_to_s3(self):
        s3_conn = boto.connect_s3()
        bucket = s3_conn.get_bucket('daas.shume.in')
        k = boto.s3.key.Key(bucket)
        k.key = self.checksum
        self.temp.seek(0)                   #move fp to head of file
        k.set_contents_from_file(self.temp)

if __name__ == '__main__':

    while(True):
        #get (url) from q
        queue = boto.connect_sqs().get_queue('daas')
        message = queue.read(5)
        if message == None :
            time.sleep(30)
        else :
            url = message.get_body()
            print '[GET] ', url
            task = Task(url)
            worker = Worker(task)
            worker.start()
            queue.delete_message(message)