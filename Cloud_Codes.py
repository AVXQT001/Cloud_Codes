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
    
  def __repr__(self):
    return filter(is_prime, range(1, self.n+1))
