fname = raw_input("Enter file name: ")
#desired output: Average spam confidence: 0.7507185185185187
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number

average = total/count
print ("Average spam confidence:",average)