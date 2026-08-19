#create a project that uses a while loop to countdown and uses a for loop to sound an alarm

import time

count_down = 6
while count_down > 0:
   print(count_down)
   time.sleep(1)
   count_down -=1  
print("kick start")

for i in range(6):
   if i == 2:
      break
   print("\nget ready for your day!")