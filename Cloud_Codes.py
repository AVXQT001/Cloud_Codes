import os, datetime

def info():                                                                                                                        
  print("Welcome to Cloud Imports!")
  
def is_prime(num: int):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

class prime:
  def __init__(self, n):
    self.n = n
    ans = filter(is_prime, range(1, self.n+1))
    
  def __repr__(self):
    return ans               

  def __str__(self):
    return str(list(ans))
