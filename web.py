from bottle import run, template, request, get, post, redirect
from task import Task

@get('/')
def index():
    # rs = ({'url': 'test.com', 'status': 'finish'},)
    rs = None
    return template('index.tpl', results=rs)

@post('/download')
def download():
    url = request.forms.get('url')
    task = Task(url)
    task.enqueue()
    redirect('/')


run(host='localhost', port=8080)