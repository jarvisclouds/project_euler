# find the largest prime factor

def is_prime(x):
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True
      
      
        
num = 600851475143
primes = []
primes.append(1)


for i in range(2, int(num**0.5) + 1):
  if num % i == 0:
    if is_prime(i):
      primes.append(i)
          
print(max(primes))