import random

def function(x):
    return x**3

while True:
    x1 = random.randint(-100, 100)
    if function(x1) > 0:
        x2 = random.randint(-100, 100)
        if function(x2) < 0:
            print(x1, x2)
            break

for i in range(10_000_000):
         #start false position here
         x3 = x1 - ((x2 - x1)*function(x1))/(function(x2) - function(x1))
         if (function(x3) > 0):
             x1 = x3
         elif function(x3) < 0:
             x2 = x3
         else:
              x3 = 0
              break
print(x1, x2, x3)

