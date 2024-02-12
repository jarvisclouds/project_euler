# find the sum of the even terms in the fibonacci sequence under 4 million

x = 1
y = 2
nth_term = 0
sum = 2

while True:
  nth_term = x + y
  x = y
  y = nth_term
  
  if nth_term % 2 == 0:
    sum += nth_term
    
  if not (nth_term <= 4000000):
    break
  
print(sum)