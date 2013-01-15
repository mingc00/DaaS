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
        # check wheather the task is existed
        if task.is_dup():
            print "dup"
            return

        self.task.add_to_db()
        m = hashlib.sha1()

        #TODO: start downloading
        print "download" + url

        f = urlopen(url)
        BLOCKSIZE = 4 * 1024 * 1024

        self.temp = tempfile.TemporaryFile()
        while True:
            data = data = f.read(BLOCKSIZE)
            if not data:
                break
            self.temp.write(data)
            m.update(data)

        # after
        self.checksum = m.hexdigest()
        self.task.finish(self.checksum, os.path.basename(url))
        self.save_to_s3()

    def save_to_s3(self):
        #TODO
        print "save to s3..."
        s3_conn = boto.connect_s3()
        bucket = s3_conn.get_bucket('daas.shume.in')
        k = boto.s3.key.Key(bucket)
        self.temp.seek(0)                   #move fp to head of file
        k.set_contents_from_file(self.temp)

if __name__ == '__main__':

    while(True):

        #get (url) from q
        queue = boto.connect_sqs().get_queue('daas')
        message = queue.read(5)
        if message == None :
            print "sleeping"
            time.sleep(30)
            print "wake up"
        else :
            url = message.get_body()

            url = 'http://dl.dropbox.com/u/92223375/setting6.png'
            task = Task(url)
            worker = Worker(task)
            worker.start()