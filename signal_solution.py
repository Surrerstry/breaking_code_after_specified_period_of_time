#!/usr/bin/env python2

from signal import alarm, signal, SIGALRM
from time import sleep

class TimeoutException(Exception):
   def __init__(self, *args, **kwargs):
      Exception.__init__(self, *args, **kwargs)

def active_alarm(signum, stack):
   raise TimeoutException('Working time of function exceeded limit')

signal(SIGALRM, active_alarm)
alarm(1)

sleep(0.5)
print('Here everything is all right yet...')

try:
   sleep(10)
except TimeoutException:
   print('Time exceeded...')

