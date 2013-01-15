from bottle import run, template, request, get, post
from task import Task

@get('/')
def index():
    return template('index.html')

@post('/download')
def download():
    url = request.forms.get('url')
    task = Task(url)
    task.enqueue()


run(host='localhost', port=8080)