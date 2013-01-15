from bottle import run, template, request, get, post, redirect
from helper import list_all, get_url
from task import Task

@get('/')
def index():
    rs = list_all()
    # rs = ({'url': 'test.com', 'status': 'finish'},)
    rs = None
    return template('index.tpl', results=rs)

@post('/add')
def add():
    url = request.forms.get('url')
    task = Task(url)
    task.enqueue()
    redirect('/')

@get('/download/<checksum>/<filename>')
def download(checksum, filename):
    redirect(get_url(checksum, filename))

run(host='localhost', port=8080)