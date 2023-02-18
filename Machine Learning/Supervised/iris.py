# Importing libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Loading the iris dataset
iris = datasets.load_iris()
X=iris.data
y=iris.target

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

# Training the decision tree classifier on the training data
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)

# Testing the classifier on the testing data
accuracy = clf.score(X_test, y_test)
print("Accuracy: ", accuracy)