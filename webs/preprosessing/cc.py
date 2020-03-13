import pandas as pd
data = pd.read_csv('happy.csv',header=None,usecols=[1])
ccdata = data.sample(20)
print(ccdata)