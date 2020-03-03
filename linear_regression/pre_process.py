import pandas as pd


housing = pd.read_csv('kc_train.csv',header=None)

housing1 = housing.ix[:,1]
housing2 = housing.ix[:, (x for x in range(0, len(housing.columns)) if x != 1)]

housing1.to_csv('kc_train1.csv',index=False,header=False)
housing2.to_csv('kc_train2.csv',index=False,header=False)
print(housing1.count)
print(housing2.count)

