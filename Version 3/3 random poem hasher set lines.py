### TeCoEd###
# June 2021 #

import shutil
from pathlib import Path
import random
import time

print ("Welcome")
line_length = int(input("How many words per line do you want? "))
to_store = [] # stores final poem before writing to file

###############################
#   Read the Poem files       #
###############################

# open poem one and read
p1_lines = []

file = open('Poem1', 'r')
for line in file:
    for word in line.split():
        p1_lines.append(word + " ")
        #print (word)

file.close()

# open poem two and read
p2_lines = []
file2 = open('Poem2', 'r')
for line in file2:
    for word in line.split():
        p2_lines.append(word + " ")
        #print (word)

file2.close()

###############################
# Combines the two poem files #
###############################

firstfile = p1_lines
secondfile = p2_lines

# copy first poem file to second poem file
for x in firstfile:
    secondfile.append(x)

# switch variable name
final_file = secondfile

# print (final_file) '''test print '''

print (len(final_file))
tw = (len(final_file)) # total words

for i in range (len(final_file)):
    random_word = random.randrange(len(final_file))
    #print (final_file[random_word])
    final_file.append(final_file[random_word])
    del final_file[random_word]

# print (final_file) # this is the combined poem in a list

# how many words per line
for i in range (0, len(final_file), line_length):
    #print (final_file[i:i+line_length])
    to_store.append(final_file[i:i+line_length])

#a ppend the lines to to_store'###
#print (to_store) test the lines are added to the array

###############################
#       Write to a file       #
###############################
newfile = input("Enter the name of the new file: ")
print()
print("The merged content of the 2 files will be in", newfile)


MyFile=open(newfile,'w')
for x in to_store:
    MyFile.writelines(x)
    MyFile.write('\n')
MyFile.close()


print("\nThe content is merged successfully.!")




