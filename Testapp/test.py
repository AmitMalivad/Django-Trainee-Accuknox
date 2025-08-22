from django.contrib.auth.models import User
import time

import threading

from django.db import transaction


start = time.time()
User.objects.create(username="test_user")
end = time.time()

print(f"Total time taken: {end - start} seconds")


print("Caller thread:", threading.current_thread().name)
User.objects.create(username="thread_test")


try:
    with transaction.atomic():
        User.objects.create(username="txn_test")
        raise Exception("Force rollback!")
except:
    pass

print("Row count after rollback:", User.objects.filter(username="txn_test").count())