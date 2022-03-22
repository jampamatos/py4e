#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input("Enter file name:")
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhandler = open(fname)
except:
    print("No such file name!")
    quit()

hour_count = dict()
for line in fhandler:
    if line.startswith("From") and len(line.split()) > 2:
            line_words = line.split()
            hour = line_words[5].split(':')
            hour_count[hour[0]] = hour_count.get(hour[0], 0) + 1
            
sorted_hour = (sorted([(k,v) for k,v in hour_count.items()]))

for key, val in sorted_hour:
    print (key, val)