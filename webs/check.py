
import csv
import pandas as pd
import re

emlist1 = []
emlist2 = []
emlist3 = []
emlist4 = []
emlist5 = []
emlist6 = []
#Make a vocabulary retrieval lexicon
with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'joy' in row:
            if '1' in row:
                emlist1.append(row)

    print(emlist1)
    print(len(emlist1))
finlex=pd.DataFrame(columns=None,data=emlist1)
finlex.to_csv('happyLex.csv',header = None,index= None,encoding='utf-8')

with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'positive' in row:
            if '1' in row:
                emlist2.append(row)

    print(emlist2)
    print(len(emlist2))
finlex=pd.DataFrame(columns=None,data=emlist2)
finlex.to_csv('PleasantLex.csv',header = None,index= None,encoding='utf-8')

with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'fear' in row:
            if '1' in row:
                emlist3.append(row)

    print(emlist3)
    print(len(emlist3))
finlex=pd.DataFrame(columns=None,data=emlist3)
finlex.to_csv('fearLex.csv',header = None,index= None,encoding='utf-8')

with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'surprise' in row:
            if '1' in row:
                emlist4.append(row)

    print(emlist4)
    print(len(emlist4))
finlex=pd.DataFrame(columns=None,data=emlist4)
finlex.to_csv('surpriseLex.csv',header = None,index= None,encoding='utf-8')

with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'anger' in row:
            if '1' in row:
                emlist5.append(row)

    print(emlist5)
    print(len(emlist5))
finlex=pd.DataFrame(columns=None,data=emlist5)
finlex.to_csv('angryLex.csv',header = None,index= None,encoding='utf-8')

with open('lexicon.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

        if 'anticipation' in row:
            if '1' in row:
                emlist6.append(row)

    print(emlist6)
    print(len(emlist6))
finlex=pd.DataFrame(columns=None,data=emlist6)
finlex.to_csv('exticeLex.csv',header = None,index= None,encoding='utf-8')




