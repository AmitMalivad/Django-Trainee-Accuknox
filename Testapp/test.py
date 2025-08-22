from django.contrib.auth.models import User
import time

import threading


start = time.time()
User.objects.create(username="test_user")
end = time.time()

print(f"Total time taken: {end - start} seconds")


print("Caller thread:", threading.current_thread().name)
User.objects.create(username="thread_test")