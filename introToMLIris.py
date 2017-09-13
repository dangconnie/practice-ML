# Tutorial from: https://github.com/gwpjp/Teaching/blob/master/.ipynb_checkpoints/IntrotoMLIris-checkpoint.ipynb

# pandas - contains data analysis tools and a convenient data structure

# matplotlib - tools for plotting data, especially using the sub-library pyplot


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++ STEP 0: Import Libraries +++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
import pandas
import matplotlib.pyplot as plt #sets plt as a shortcut so that we don't have to write the entire name each time

# =====================================================
# ================ SUPER IMPORTANT ====================
# =====================================================
import requests
requests.packages.urllib3.disable_warnings()

# "If you have installed Python 3.6 on OSX and are getting the "SSL: CERTIFICATE_VERIFY_FAILED" error when trying to connect to an https:// site, it's probably because Python 3.6 on OSX has no certificates at all, and can't validate any SSL connections. This is a change for 3.6 on OSX, and requires a post-install step, which installs the certifi package of certificates. This is documented in the ReadMe, which you should find at /Applications/Python\ 3.6/ReadMe.rtf

# The ReadMe will have you run this post-install script, which just installs certifi: /Applications/Python\ 3.6/Install\ Certificates.command "

# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error

# Fix problem with exception handling or installing certifi

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context



# =====================================================
# =====================================================
# =====================================================




# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++ STEP 1: Get the Data +++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# Get file from website. Read it and load it without headers. We're using the iris dataset.
iris = pandas.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)




# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++ STEP 2: Get to know the data +++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# Rename columns:
iris.columns = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species']

# Show the first 5 rows from the dataset
iris.head(5)

# Show the last 5 rows from the dataset
iris.tail(5)

# Get the size of our dataset
iris.shape # outputs (150, 5). There are 150 rows and 5 columns in this dataset

# Get some overall info about our dataset and what type of data it contains.
iris.info()



# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++ STEP 3: Exploratory Data Analysis By Plotting +++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# Time to plot the data in various ways.
# How are sepal length and width are related for each species?

fig = iris[iris.Species=='Iris-setosa'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='orange', label='setosa')

iris[iris.Species=='Iris-versicolor'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='blue', label='versicolor',ax=fig)

iris[iris.Species=='Iris-virginica'].plot(kind='scatter',x='SepalLengthCm',y='SepalWidthCm',color='green', label='virginica', ax=fig)

fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal Width")
fig.set_title("Sepal Length vs. Sepal Width")
fig=plt.gcf() #gcf() = get a reference to the current figure
fig.set_size_inches(12,6)
plt.show() #show() - displays a figure


# How about the relationship between petal length and width?
fig = iris[iris.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='orange', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='blue', label='versicolor',ax=fig)
iris[iris.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm',y='PetalWidthCm',color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length vs. Petal Width")
fig=plt.gcf()
fig.set_size_inches(12,6)
plt.show()

 # It seems that petal features do much better than sepal features in clustering the data. 



# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++ STEP 4: Build our model ++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

inputs = iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
outputs = iris['Species']



# As the name suggests, the k-nearest neighbors (kNN) algorithm works by looking at other points that are 'near by' to determine which species to assign. For our first model, we are going to use k = 3 to look at the 3 nearest neighbors.
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics #for checking the model accuracy

model = KNeighborsClassifier(n_neighbors=3) # store our model type
model.fit(inputs,outputs) # use our iris data to build our model
prediction = model.predict(inputs) # check our model's accuracy on our own iris data set
print('The accuracy of the KNN is', metrics.accuracy_score(prediction,outputs)) # prints "The accuracy of the KNN is 0.96" --> 96% accuracy


 # Let's take a look at which pieces of data were not predicted accurately. (Where the prediction did no equal the outputs)
iris2 = pandas.concat([iris,pandas.DataFrame(prediction,columns=["PredictedSpecies"])],axis=1)
iris2[prediction != outputs]


# These 6 pieces of data have their species picked incorrectly. Let's see if we can improve our model's accuracy. Our k-nearest neighbors algorithm has a parameter that we can vary, k. By changing k, we can often improve our model's ability to accurately predict the species of our training data. We will apply the same algorithm with k = 5, 7, and 10.

model = KNeighborsClassifier(n_neighbors=5) # store our model type
model.fit(inputs,outputs) # use our iris data to build our model
prediction = model.predict(inputs) # check our model's accuracy on our own iris data set
print('The accuracy of the KNN is', metrics.accuracy_score(prediction,outputs))

# The accuracy of the KNN is 0.966666666667



model = KNeighborsClassifier(n_neighbors=7) # store our model type
model.fit(inputs,outputs) # use our iris data to build our model
prediction = model.predict(inputs) # check our model's accuracy on our own iris data set
print('The accuracy of the KNN is', metrics.accuracy_score(prediction,outputs))

# The accuracy of the KNN is 0.973333333333




model = KNeighborsClassifier(n_neighbors=10) # store our model type
model.fit(inputs,outputs) # use our iris data to build our model
prediction = model.predict(inputs) # check our model's accuracy on our own iris data set
print('The accuracy of the KNN is', metrics.accuracy_score(prediction,outputs))


# The accuracy of the KNN is 0.98


# It seems like increasing k was a good decision, but be careful! Our goal is to predict new data - not to accurately predict our training data. As we increase k, we are increasing our bias.


# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++ STEP 5: Use our model to make predictions +++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

# Some new data has been collected!


new = pandas.read_csv("https://raw.githubusercontent.com/gwpjp/Teaching/master/new_data.csv")
new.columns = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
new


# We will now use our model to predict the species for this new data. We will use our latest model with k = 10.

predictNew = model.predict(new)
print(predictNew)


new2 = pandas.concat([new,pandas.DataFrame(predictNew,columns=["Species"])],axis=1)
print(new2)




# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++ Support Vector Machines (SVM) +++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

#  another common machine learning algorithm.


from sklearn import svm  
modelSVM = svm.SVC() # store our new model type
modelSVM.fit(inputs,outputs) 
predictionSVM = modelSVM.predict(inputs) 
print('The accuracy of the KNN is', metrics.accuracy_score(predictionSVM,outputs))