import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

import threading

from django.db import connection


@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal handler started...")
    time.sleep(5) 
    print("Signal handler finished!")


@receiver(post_save, sender=User)
def thread_checker(sender, instance, **kwargs):
    print("Signal handler thread:", threading.current_thread().name)


@receiver(post_save, sender=User)
def transaction_checker(sender, instance, **kwargs):
    print("Signal handler running...")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username='txn_test'")
    print("Row count inside signal:", cursor.fetchone()[0])