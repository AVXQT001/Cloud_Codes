import os, datetime

def info():                                                                                                                        
  print("Welcome to Cloud Imports!")
  
def is_prime(num: int):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def prime(n):                                        
  return filter(is_prime, range(1, n+1))
