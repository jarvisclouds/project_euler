# find the smallest positive number that's evenly divisible by 1-20

def is_div(num):
  for i in range(2,21):
    if num % i != 0:
      return False
    
  return True

num = 1

while is_div(num) == False:
  num += 1
    
print(num)