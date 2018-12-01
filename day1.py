import os

fname = 'input.txt'
index = 0
intArray = []
freqArray = []
match = 0


for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        n = int(line)
        intArray.append(n)

freqArray.append(intArray[0])
for x in range(1, len(intArray)):
    freq = intArray[x]+ freqArray[x -1]
    if freq in freqArray:
        print "Match found at: " + freq
        match += 1
    freqArray.append(freq)

while (match != 1):
    indexOfIntArray = index % len(intArray)
    freq = intArray[indexOfIntArray] + freqArray[len(freqArray) - 1]
    if freq in freqArray:
        print ("Match found at: %d",freq)
        print(len(freqArray))
        match += 1

    freqArray.append(freq)

    index += 1
