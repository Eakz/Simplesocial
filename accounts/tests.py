from django.test import TestCase
import time, datetime, sys
# Create your tests here.
while True:
    print(datetime.datetime.now().strftime('%H:%M:%S'), end='', flush=True)
    time.sleep(1)
    sys.stdout.flush()
    print('\r', end='', flush=True)
