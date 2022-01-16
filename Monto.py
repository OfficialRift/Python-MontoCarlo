import random
  
inside_points= 0
outside_points= 0
  
for i in range(100000):
    x= random.uniform(-1, 1) # between 0 and 1
    y= random.uniform(-1, 1)
  
    if x**2 + y**2<= 1:
        inside_points+= 1
  
    outside_points+= 1
  
    pi = 4* inside_points/ outside_points
    print("Pi= ", pi)