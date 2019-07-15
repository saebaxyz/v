import random
def my_shuffle(array):
   random.shuffle(array)
   return array
        
ko =['hearts', 'spades', 'clubs', 'diamonds']

#for suit in my_shuffle(['hearts', 'spades', 'clubs', 'diamonds']):
for suit in my_shuffle(ko) :
  print suit
  
print '----------------'