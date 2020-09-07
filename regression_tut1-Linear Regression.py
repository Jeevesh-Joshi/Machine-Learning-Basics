import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()

# print(diabetes.keys()) #It tell what's present inside the database 
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename']

# print(diabetes.data) #Gives us the data present inside
# print(diabetes.data.shape) #Gives us the shape/dimension of the data present inside
# print(diabetes.DESCR) #Tells us about the data present inside

# diabetes_X = diabetes.data #complete dataset

diabetes_X = diabetes.data[:,np.newaxis,2] 
#inorder to retrive only 1 feature and 1 label : [,2] here tells to get the 2nd feature i.e 2nd column of all data entries.
#  numpy.newaxis is used to increase the dimension of the existing array by one more dimension, when used once. 

# print(diabetes_X)

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]
# print(len(diabetes.target)) #target gives us label.

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-30:]

# using linear_model to train our data

model = linear_model.LinearRegression()

# training our model to get the best linear f(x)n/line 
model.fit(diabetes_X_train,diabetes_Y_train)

# testing our model
diabetes_Y_predicted = model.predict(diabetes_X_test)

# calculating avg mean square error
error = mean_squared_error(diabetes_Y_test, diabetes_Y_predicted)
print("MSE :", error)

print("Weights :", model.coef_)
print("Intercepts :", model.intercept_)

# plotting our f(x)n //won't work if we use multiple features, here using only 1.
plt.scatter(diabetes_X_train, diabetes_Y_train)
# plt.scatter(diabetes_X_test, diabetes_Y_test)
# plt.scatter(diabetes_X_test, diabetes_Y_predicted)
# plt.plot(diabetes_X_test, diabetes_Y_test)
plt.plot(diabetes_X_test, diabetes_Y_predicted)
plt.show()
