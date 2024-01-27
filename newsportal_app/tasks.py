'''
py manage.py runserver
open redis-server.exe as administrator
celery -A newsportal_project worker -l INFO --pool=solo
'''


from celery import shared_task
import time


@shared_task
def hello():
    print("Hello, from tasks.py")


@shared_task
def printer(N):
    for i in range(N):
        print(i+1)

