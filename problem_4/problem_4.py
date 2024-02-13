# find the largest palindrome made the product of two 3-digit numbers
# palindrome = the same both ways ex. 9009

def is_palindrome(num):
  if str(num) == str(num)[::-1]:
    return True
  return False

multiple = 0

for i in range(100,1000):
  for j in range(100,1000):
    
    x = i * j
    
    if is_palindrome(x):
      if x > multiple:
        multiple = x

print(multiple)