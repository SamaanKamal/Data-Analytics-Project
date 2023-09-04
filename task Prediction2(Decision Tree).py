import pandas as pd 
from sklearn import tree
from sklearn.tree import export_graphviz 
import graphviz

data=pd.read_csv(r"../../../../Users/User/Desktop/Python/camera_dataset.csv")
print(data)

data.info()
data.dropna(axis=0,inplace=True)


x=data[['Release date','Max resolution','Low resolution',
        'Effective pixels','Zoom wide (W)','Zoom tele (T)',
        'Normal focus range','Macro focus range','Storage included',
        'Dimensions','Weight (inc. batteries)']]

y=data['Price']


model = tree.DecisionTreeRegressor()
model.fit(x,y)
predictions = model.predict(x)

print(model.feature_importances_)

# export the decision tree to a tree.dot file
export_graphviz(model , out_file = 'DecisionTree.dot')

with open('DecisionTree.dot') as f:
   dot_graph = f.read()

g = graphviz.Source(dot_graph)
g.render()
print('POF created')
