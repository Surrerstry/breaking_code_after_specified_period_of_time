#!/usr/bin/env python2

from threading import Thread
from time import time, sleep

# necessary to get return value from thread
class ThreadWithReturnValue(Thread):
   
   def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
      Thread.__init__(self, group, target, name, args, kwargs)
      self._return = None

   def run(self):
      if self._Thread__target is not None:
         self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

   def join(self):
      return self._return

def sandbox(func_name, max_time, args=tuple()):
   """
   >>> sandbox(test_function, 5, ['A', 'B', 'C'])
   ('Function finished correctly', ['C', 'B', 'A'])
   >>> sandbox(test_function, 0.1, ['D', 'E', 'F'])
   'Function forcibly killed'
   >>> sandbox(test_function, 0.1)
   'Function forcibly killed'
   """

   if not callable(func_name):
      raise Exception('FirstArgumentNotCallable')
   if not isinstance(max_time, (int, float)):
      raise Exception('SecondArgumentNotANumber')

   args = args or tuple()

   thread_object = ThreadWithReturnValue(target=func_name, args=args)
   start_time = time()
   thread_object.start()

   while True:
      if not thread_object.isAlive():
         break
      elif time() - start_time > max_time:
         thread_object._Thread__stop()
         #thread_object._Thread__delete()
         # it cause KeyError somehow, but it seems to be not necessary
         return 'Function forcibly killed'

   return 'Function finished correctly', thread_object.join()

# test function for doctests:
def test_function(a=None, b=None, c=None):
   """
   >>> test_function('X', 'Y', 'Z')
   ['Z', 'Y', 'X']
   >>> test_function()
   [None, None, None]
   """
   #print(a, b, c)
   sleep(3)
   return [c, b, a]

if __name__ == '__main__':
   import doctest
   doctest.testmod()
   # Samples of usage:
   #print(sandbox(test_function, 5, ['A', 'B', 'C']))
   #print(sandbox(test_function, 0.1, ['A', 'B', 'C']))
   #print(sandbox(test_function, 0.1))

