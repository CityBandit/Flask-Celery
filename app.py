import os
import time 
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

broker_url = os.environ.get("BROKER_URL")
result_backend = os.environ.get("RESULT_BACKEND")

celery = Celery("app", broker=broker_url, backend=result_backend)


@celery.task
def add(x, y):
    time.sleep(10)
    return x + y
