import pandas as pd

#The random selects samples for crowdsourcing
ccdata = []


data1 = pd.read_csv('happy.csv',header=None,index_col=0)
data2 = pd.read_csv('Ecitement.csv',header=None,index_col=0)
data3 = pd.read_csv('pleasant.csv',header=None,index_col=0)
data4 = pd.read_csv('fear.csv',header=None,index_col=0)
data5 = pd.read_csv('surprise.csv',header=None,index_col=0)
data6 = pd.read_csv('angry.csv',header=None,index_col=0)
ecdata = data2.sample(20)
ecdata=pd.DataFrame(columns=None,data=ecdata)
ecdata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample1.csv',header=0,encoding='gbk')

hpdata = data1.sample(20)
hpdata=pd.DataFrame(columns=None,data=hpdata)
hpdata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample2.csv',header=0,encoding='gbk')

pldata = data3.sample(20)
pldata=pd.DataFrame(columns=None,data=pldata)
pldata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample3.csv',header=0,encoding='gbk')

fedata = data4.sample(20)
fedata=pd.DataFrame(columns=None,data=fedata)
fedata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample4.csv',header=0,encoding='gbk')

sudata = data5.sample(20)
sudata=pd.DataFrame(columns=None,data=sudata)
sudata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample5.csv',header=0,encoding='gbk')

andata = data6.sample(20)
andata=pd.DataFrame(columns=None,data=andata)
andata.to_csv('C:\\Users\\fz\\Documents\\webs\\samples\\sample6.csv',header=0,encoding='gbk')


