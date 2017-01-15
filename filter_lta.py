import re
import os
import glob
data_dir = '/data2/gmrtarch/cycle20/'
VALID_LIST = '/data2/shubhankar/parser/healthy2_file.txt'
valid_observations = open(VALID_LIST, 'r').read().split('\n')[0:-1]
all_observations = os.listdir(data_dir)
for DIR_NAME in all_observations:
    current_obslog = glob.glob(data_dir+DIR_NAME+'/'+'*.obslog')
    """
    if current_obslog == []:
        print DIR_NAME
        break
    """
    #Extract substring that contains obslog relative path
    relative_path = re.findall(r'[/][\d]+[.]obslog', current_obslog[0])[0][1:] 
    #Invalid file (not fitting given constraints i.e. < 900 MHz and IF BW != 6,16,32)
    if relative_path not in valid_observations:
        print data_dir+DIR_NAME
    #Valid obslog file with no LTA file in the DIR
    """
    if relative_path in valid_observations:
        if glob.glob(data_dir+DIR_NAME+'/'+'*.lta') == []:
            print data_dir+DIR_NAME
    """ 
