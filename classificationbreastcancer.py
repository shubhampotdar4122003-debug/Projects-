import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

#---------------------------------------------
#step 1 : load the dataset
#---------------------------------------------

df = pd.read_csv("breast_cancer.csv")
print("shape of dataset :",df.shape)
print("first 5 records :",df.head())

#---------------------------------------------
#step 2 : seperate fetures and labels
#---------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]

#---------------------------------------------
# step 3 : split datset for traing and testing
#---------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state=42)

#---------------------------------------------
#step 4 : create boosting model(Adaboost)
#---------------------------------------------

boost_model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42)


#---------------------------------------------
#step 5 : train boosting model
#---------------------------------------------

boost_model.fit(X_train,Y_train)

#---------------------------------------------
#step 6 : test boosting model
#---------------------------------------------

Y_pred = boost_model.predict(X_test)

#---------------------------------------------
#step 7 : Evaluate boosting model
#---------------------------------------------

print("boosting Accuracy :",accuracy_score(Y_test,Y_pred))

print("confusion matrix :")
print(confusion_matrix(Y_test,Y_pred))