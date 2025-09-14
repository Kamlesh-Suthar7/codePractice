from sklearn.tree import DecisionTreeClassifier
features = [[150,0],
            [170,0],
            [130,1],
            [120,1]]
labels = ["apple","apple","orange","orange"]
clf = DecisionTreeClassifier()
clf = clf.fit(features,labels)
prediction = clf.predict([[150,1]])
type(prediction)
print(f"The fruit is {prediction[0]}")
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(11,6))
plot_tree(clf, feature_names=["weight","color"], class_names=["apple","orange"], filled=True )
