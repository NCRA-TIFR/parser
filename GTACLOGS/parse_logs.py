import os
import re
healthy1_file = open('../healthy1_file.txt', 'w')
unhealthy1_file = open('../unhealthy1_file.txt', 'w')
healthy2_file = open('../healthy2_file.txt', 'w')
unhealthy2_file = open('../unhealthy2_file.txt', 'w')

#Function to extract lines from ANTENNA to CORRELATOR | GSB (Standardized for all files across logs)
def extract(FILENAME):
    obslog = open(FILENAME).read()
    ANTENNA = obslog.find('ANTENNA')
    if(obslog.find('CORRELATOR SETTINGS') != -1):
        NEXT_SECTION = obslog.find('CORRELATOR SETTINGS')
    elif(obslog.find('CORREATOR SETTINGS') != -1):
        NEXT_SECTION = obslog.find('CORREATOR SETTINGS')
    elif(obslog.find('GSB SETTINGS') != -1):
        NEXT_SECTION = obslog.find('GSB SETTINGS') 
    EXTRACT = obslog[ANTENNA:NEXT_SECTION]
    return EXTRACT

healthy = []
unhealthy = []

#All files in the current directory
all_files = os.listdir('.')

for filename in all_files:
    print filename
    #Extracted text from the current log file
    EXTRACT = extract(filename).split('\n')
    try:
        RF = re.findall(r'\d+\s' + 'MHz', EXTRACT[2])
    except IndexError:
        unhealthy.append(filename)
        continue
    try:
        if(int(RF[0].split()[0]) < 900):
            healthy.append(filename)
        else:
            unhealthy.append(filename)
    except IndexError:
        unhealthy.append(filename)
        continue
#Removal of 1st line
for item in healthy:
    healthy1_file.write('%s\n' % item)

for item in unhealthy:
    unhealthy1_file.write('%s\n' % item)

unhealthy2 = []
healthy2 = []

#All files in the current directory

for filename in healthy:
    print filename
    #Extracted text from the current log file
    EXTRACT = extract(filename).split('\n')
    try:
        RF = re.findall(r'\d+\s' + 'MHz', EXTRACT[4])
    except IndexError:
        unhealthy2.append(filename)
        continue
    try:
        if(int(RF[0].split()[0]) == 32 or int(RF[0].split()[0]) == 32):
            healthy2.append(filename)
        else:
            unhealthy2.append(filename)
    except IndexError:
        unhealthy2.append(filename)
        continue
#Removal of 1st line
for item in healthy2:
    healthy2_file.write('%s\n' % item)

for item in unhealthy2:
    unhealthy2_file.write('%s\n' % item)
