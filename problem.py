import pandas as pd
#import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_csv('regression.csv')
print(data.describe())
y = data['GPA']
x1 = data['SAT']
plt.scatter(x1,y)
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

#x = sm.add_constant(x1)
#results = sm.OLS(y,x).fit()
#results.summary()
plt.scatter(x1,y)
yhat = 0.0017*x1 + 0.275
fig = plt.plot(x1,yhat, lw=4, c='orange', label = 'regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()
