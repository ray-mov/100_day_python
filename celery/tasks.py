from celery import Celery


app = Celery('tasks',
             broker='pyamqp://guest@localhost//',
             backend='rpc://')

@app.task
def add(x,y):
    print("TASK ARGS:", x, y)
    return x + y







# celery -A tasks worker --loglevel=INFO --pool=solo
