import boto
from boto.sqs.message import Message

class Task(object):

    def __init__(self, url):
        self.url = url
        # connect simpleDB
        self.sdb_domain = boto.connect_sdb().get_domain('daas')

    def add_to_db(self):
        item_name = self.url
        item_attr = {
            'checksum': '',
            'status': 'Queued',
            'url': self.url
        }
        self.sdb_domain.put_attributes(item_name, item_attr)

    def update_status(self, status):
        item = self.sdb_domain.get_item(self.url)
        item['status'] = status
        item.save()

    def finish(self, checksum, filename):
        item = self.sdb_domain.get_item(self.url)
        item['status'] = 'Finished'
        item['checksum'] = checksum
        item['filename'] = filename
        item.save()

    def enqueue(self):
        conn = boto.connect_sqs()
        queue = conn.get_queue('daas')
        m = Message()
        m.set_body(self.url)
        queue.write(m)
        self.add_to_db()
        return m

    def is_dup(self):
        return self.sdb_domain.get_item(self.url) != None
