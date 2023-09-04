import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from numpy import where,quantile
data = pd.read_csv(r"../../../../Users/User/Desktop/Python/camera_dataset.csv")
x = data['Price']
x = x.values.reshape(-1, 2)
lof=LocalOutlierFactor(n_neighbors=13,contamination=.03)
y_pred=lof.fit_predict(x)
print(y_pred)
lofs_index=where(y_pred == -1)
values=x[lofs_index]
print(values)
print(x)


plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0],values[:,1], color='r')
plt.show()
print(lofs_index)

#/*--------------------------
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
from numpy import where,quantile
data = pd.read_csv(r"../../../../Users/User/Desktop/Python/camera_dataset.csv")
x = data['Price']
x = x.values.reshape(-1, 2)
model = LocalOutlierFactor(n_neighbors=13)
model.fit_predict(x)
lof = model.negative_outlier_factor_
thresh = quantile(lof, .03)
print(thresh)
index = where(lof<=thresh)
values = x[index]
plt.scatter(x[:,0], x[:,1])
plt.scatter(values[:,0], values[:,1], color='r')

plt.show()