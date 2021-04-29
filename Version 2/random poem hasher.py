import shutil
from pathlib import Path
import random
import time


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

print (len(final_file))
tw = (len(final_file)) # total words

for i in range (len(final_file)):
    random_word = random.randrange(len(final_file))
    #print (final_file[random_word])
    final_file.append(final_file[random_word])
    del final_file[random_word]

# write final poem lines to the word document

to_store = final_file[tw-tw:8], "\n", final_file[(tw-tw)+8:tw-11], "\n", final_file[(tw-tw)+15:tw-5], "\n", final_file[22:26]

###############################
#       Write to a file       #
###############################
newfile = input("Enter the name of the new file: ")
print()
print("The merged content of the 2 files will be in", newfile)


MyFile=open(newfile,'w')
for x in to_store:
    MyFile.writelines(x)
MyFile.close()


print("\nThe content is merged successfully.!")




