import os
stream = os.popen('traceroute google.com')
for line in stream:
   start_index = line.find('(')
   end_index = line.find(')')
   if start_index == -1:
       continue
   ip = line[start_index+1:end_index]
   print (ip)