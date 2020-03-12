
import glob
import time
#CSV combiner
csv_list = glob.glob('*.csv')
for i in csv_list:
    fr = open(i,'rb').read()
    with open('result.csv','ab') as f:
        f.write(fr)
print(u'finish!')