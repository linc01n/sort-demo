import merge, improve
import time
def m_sort(a):
  before = time.time()
  merge.sort(a)
  after = time.time()
  return (after - before)

def i_sort(a):
  before = time.time()
  improve.sort(a)
  after = time.time()
  return (after - before)
  
def mean_m(a):
  t = 0
  for i in range(0,10):
     t = t + m_sort(a)
  print t / 10

def mean_i(a):
  t = 0
  for i in range(0,10):
    t = t + i_sort(a)
  print t/10


