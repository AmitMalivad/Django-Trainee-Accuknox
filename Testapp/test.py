from django.contrib.auth.models import User
import time

start = time.time()
User.objects.create(username="test_user")
end = time.time()

print(f"Total time taken: {end - start} seconds")