#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail 
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who 
# sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of 
# the number of times they appear in the file. After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

fname = input("Enter file name:")
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhandler = open(fname)
except:
    print("No such file name!")
    quit()

counts = dict()
for line in fhandler:
    if line.startswith('From:'):
        linewords = line.split()
        sender = linewords[1]
        counts[sender] = counts.get(sender,0) + 1

big_count = None
big_word = None

for word,count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count
print (big_word, big_count)