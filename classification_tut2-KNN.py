from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error


# Dataset created
iris = datasets.load_iris()

# print(iris.keys())

features = iris.data
label = iris.target

# creating classifier/model
clf = KNeighborsClassifier()

# training our classifier
clf.fit(features[:100],label[:100])

# predicting values
predicted = clf.predict(features[100:])

# error in prediction
error = mean_squared_error(label[100:],predicted)
print("MSE :", error)
