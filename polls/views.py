from django.http import HttpResponse
import os
import time
import threading
from itertools import count

# is not thread safe
iterator = count(start=1, step=1)

counter = 0

def index(request):
    global counter
    request_id = next(iterator)
    time.sleep(int(request.GET.get("delay", 0)))
    # for i in range(100000000):
    #     pass
    # counter += 1
    data = f"{request_id}, pid={os.getpid()}, thread={threading.get_ident()}, counter={counter}"
    return HttpResponse(data)
