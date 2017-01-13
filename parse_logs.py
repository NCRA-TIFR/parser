import os
import re
#File containing fit observations for the first parser run (RF)
healthy1_file = open('healthy1_file.txt', 'w')
unhealthy1_file = open('unhealthy1_file.txt', 'w')

#File containing fit observations for the second parser run (IF)
healthy2_file = open('healthy2_file.txt', 'w')
unhealthy2_file = open('unhealthy2_file.txt', 'w')

#Function to extract lines from ANTENNA to CORRELATOR | GSB (Standardized for all files across logs)
def extract(FILENAME):
    obslog = open('./GTACLOGS/'+FILENAME).read()
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
index_error = []

#All files in the current directory
all_files = os.listdir('./GTACLOGS')

for filename in all_files:
    #Extracted text from the current log file
    EXTRACT = extract(filename).split('\n')
    try:
        RF = re.findall(r'\d+\s' + 'MHz', EXTRACT[2])
    except IndexError:
        print("Index Error: " + filename)
        continue
    try:
        if(int(RF[0].split()[0]) < 900):
            healthy.append(filename)
        else:
            unhealthy.append(filename)
    except IndexError:
        print("Index Error: " + filename)
        continue
#Removal of 1st line
for item in healthy:
    healthy1_file.write('%s\n' % item)

for item in unhealthy:
    unhealthy1_file.write('%s\n' % item)

unhealthy2 = []
healthy2 = []

#Iterate over only 'healthy' files i.e. files successful in first parse run
for filename in healthy:
    #Extracted text from the current log file
    EXTRACT = extract(filename).split('\n')
    try:
        RF = re.findall(r'\d+\s' + 'MHz', EXTRACT[4])
    except IndexError:
        print("Index Error: " + filename)
        continue
    try:
        IF = int(RF[0].split()[0]) 
        if(IF == 32 or IF == 16):
            healthy2.append(filename, )
        else:
            unhealthy2.append(filename)
    except IndexError:
        print("Index Error: " + filename)
        continue
#Removal of 1st line
for item in healthy2:
    healthy2_file.write('%s\n' % item)

for item in unhealthy2:
    unhealthy2_file.write('%s\n' % item)
