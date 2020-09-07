from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import numpy as np

# Train a Logistic Regression classifier to predict whether a flower is Iris verginica or not

iris = datasets.load_iris()

# print(iris.keys())
X = iris["data"][:,3:] # slicing leads to --> all rows and 3rd column only
Y = (iris["target"]==2) # will return True if target==2 else False
Y = Y.astype(np.int) # Converts True to 1 and False to 0

# print(X,Y)

# Training a Logistic Regression classifier
clf = LogisticRegression()

# training our model
clf.fit(X,Y)

# Prediction
# clf.predict()

# Using matplotlib to plot the visualiasation
X_new = np.linspace(0,3,1000) # give 1000 points bw 0-3
X_new = X_new.reshape(-1,1) # reshape to 1D array
Y_prob = clf.predict_proba(X_new)   # Tells actual value of probability

plt.plot(X_new, Y_prob[:,1], "g-", label="virginica")
plt.show()
