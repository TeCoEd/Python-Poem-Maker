import shutil 
from pathlib import Path
import random
import time


###############################
#   Read the Poem files       #
###############################

# open poem one and read
p1_lines = []
file = open("Poem1")
for line in file:
    p1_lines.append(line)
 
file.close()

# open poem two and read
p2_lines = []
file = open("Poem2")
for line in file:
    p2_lines.append(line)
 
file.close()

###############################
# Combines the two poem files #
###############################

firstfile = p1_lines
secondfile = p2_lines
merged_poem =[]

# copy first poem file to second poem file
for x in firstfile:
    secondfile.append(x)
   
# switch variable name
final_file = secondfile
    
print (len(final_file))

random.shuffle(final_file)

#print the random poem
'''for x in final_file:
    print (x)
    time.sleep(1.5)'''
   
###############################
#       Write to a file       #
###############################
newfile = input("Enter the name of the new file: ") 
print() 
print("The merged content of the 2 files will be in", newfile) 


MyFile=open(newfile,'w')
for x in final_file:
    MyFile.writelines(x)
MyFile.close()    
           
  
print("\nThe content is merged successfully.!") 




