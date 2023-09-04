#                        //prediction///
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics
data = pd.read_csv(r"../../../../Users/User/Desktop/Python/camera_dataset.csv")
print(data.head(5))

data.info()
data.drop(labels='Model',axis=1 ,inplace=True)
data.dropna(axis=0,inplace=True)
data.info()

x=data[['Release date','Max resolution','Low resolution','Effective pixels','Zoom wide (W)','Zoom tele (T)','Normal focus range','Macro focus range','Storage included','Weight (inc. batteries)','Dimensions']]
y=data['Price']

#plt.scatter(x['Max resolution'], y)
#plt.scatter(x['Weight (inc. batteries)'], y)

model=linear_model.LinearRegression()
model.fit(x,y)
prediction = model.predict(x)
print("Coef:",model.coef_)
print("Mean Square Error:",metrics.mean_squared_error(y, prediction))

plt.plot_date(x, y)

for index in range(len(prediction)):
    if(index < 5):
       print('Actual: ',y[index],'\t\t\t','Prtdicttd:',prediction[index])
    else:
        break