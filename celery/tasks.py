from celery import Celert

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x,y):
    return x + y