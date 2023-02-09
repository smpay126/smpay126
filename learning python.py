filename=input("Enter file name:")       #taking file name from user
file=open(filename,"r")               #opening the file for read operation
line_count=0                   #initializing the variables to count
word_count=0
char_count=0
for line in file:               #taking line by line from file
   l=line.split(" ")           #split the line by using spaces and store it into list l
   line_count=line_count+1           #incrementing the line count
   word_count=word_count+len(l)       #adding no.of words in list l to word_count
   char_count=char_count+len(line)       #adding no.of characters in the line to char_count
file.close()                   #after reading file closing the file
print("lines ", line_count)               #printing the counts
print("words ", word_count)
print("characters", char_count)