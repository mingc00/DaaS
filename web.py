from bottle import run, template, request, get, post, redirect, default_app
from helper import list_all, get_url
from task import Task

@get('/')
def index():
    rs = list_all()
    return template('views/index.tpl', results=rs)

@post('/add')
def add():
    url = request.forms.get('url')
    task = Task(url)
    if not task.is_dup():
        task.add_to_db()
        task.enqueue()
    redirect('/')

@get('/download/<checksum>/<filename>')
def download(checksum, filename):
    redirect(get_url(checksum, filename))

if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
else:
    application = default_app()
