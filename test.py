import os
import time
import threading

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestProject.settings")
import django
django.setup()

from django.contrib.auth.models import User
from django.db import transaction

# Q-1
start = time.time()
User.objects.create(username=f"test_user_{int(time.time())}") 
end = time.time()
print(f"Q1 - Total time taken: {end - start} seconds")

# Q-2
print("Q2 - Caller thread:", threading.current_thread().name)
User.objects.create(username=f"thread_test_{int(time.time())}")  

# Q-3
try:
    with transaction.atomic():
        User.objects.create(username=f"txn_test_{int(time.time())}") 
        raise Exception("Force rollback!")  
except:
    pass

print("Q3 - Row count after rollback:",
      User.objects.filter(username__startswith="txn_test_").count())
