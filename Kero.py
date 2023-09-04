#                        //data cleaning and visualization ///
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

dataset = pd.read_csv("../../../../Users/User/Desktop/Python/camera_dataset.csv")

plt.scatter(dataset['Release date'],dataset['Max resolution'])
plt.title("scatter plot of max resolution over the years")
plt.xlabel('Release date')
plt.ylabel('Max resolution')
plt.colorbar()
plt.show()




sns.distplot(dataset['Storage included'])
plt.show()

