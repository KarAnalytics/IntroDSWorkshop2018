## Objective: Fit simple linear regression model using R

## We have to import some libraries so that we can load the data
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as sm

adv = pd.read_csv("https://raw.githubusercontent.com/KarAnalytics/IntroDSWorkshop2018/master/Advertising.csv")

plt.scatter(adv['TV'],adv['Sales'])
plt.scatter(adv['Radio'],adv['Sales'])
plt.scatter(adv['Newspaper'],adv['Sales'])

result = sm.ols(formula="Sales ~ TV + Newspaper + Radio", data=adv).fit()
print(result.summary())
