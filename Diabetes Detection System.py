import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier



# Step 1 : Exploratory Data Analysis(EDA)

print("Step 1 : Exploratory Data Analysis(EDA)".center(100,"="))

border =(100 * "=")


df = pd.read_csv('diabetes.csv')
print("Displaying first 5 rows : ")
print(df.head())
print(border)

print("checking column info : ")
print(df.info())
print(border)

print("Checking null values : ")
print(df.isnull().sum())
print(border)

print("Displaying basic Statistic : ")
print(df.describe())
print(border)

print("Distribution of the target variable")
plt.figure(figsize =(8,4))
sns.countplot(x ='Outcome' , data = df)
plt.title("Distribution of the target variable ")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.show()
print(border)

print("Distribution of feature" )
df.hist(figsize = (12,10),bins = 20)
plt.tight_layout()
plt.show()
print(border)

print("checking outliers")
plt.figure(figsize = (10,6))
sns.boxplot(data = df)
plt.xticks(rotation = 45)
plt.title("boxplot of features")
plt.show()
print(border)

print("checking patterns")
sns.pairplot(df, hue = 'Outcome')
plt.show()
print(border)

# Step 2 : data Preprocessing

print("Step 2 : data Preprocessing".center(100,"="))
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

print("Zero values before handling:")
print((df[cols] == 0).sum())

df[cols] = df[cols].replace(0, np.nan)

print("\nMissing values after replacing 0 with NaN:")
print(df[cols].isnull().sum())

for col in cols:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing values after handling:")
print(df[cols].isnull().sum())
print(border)

print("Feature scaling using Standard Scalling")
scaler = StandardScaler()
print(border)

print("spliting dataset as features and target")
X = df.drop(["Outcome"],axis = 1)
Y = df["Outcome"]

X_scaler = scaler.fit_transform(X)
print("Scalled value of feature :",X_scaler)
print(border)

# Step 3 : Model Building

print("Step 3 : Model Building")

X_train,X_test,Y_train,Y_test = train_test_split(X_scaler,Y,test_size = 0.2,random_state = 42)

lr_model = LogisticRegression()
de_model = DecisionTreeClassifier()
KNN_model = KNeighborsClassifier(n_neighbors = 3)

lr_model.fit(X_train,Y_train)
de_model.fit(X_train,Y_train)
KNN_model.fit(X_train,Y_train)

Y_predlr = lr_model.predict(X_test)
Y_predde = de_model.predict(X_test)
KNN_pred = KNN_model.predict(X_test)

# Step 4 : Model Evaluation
print(' Step 4 : Model Evaluation'.center(100,"="))

print("Accuracy of models which have trained :")

Accuracy_lr = accuracy_score(Y_predlr,Y_test)
print("Model Accuray of Logistic Regression :",Accuracy_lr * 100)
print(border)

Accuracy_de = accuracy_score(Y_predde,Y_test)
print("Model Accuray of Decision Tree Classifier :",Accuracy_de * 100)
print(border)

Accuracy_KNN = accuracy_score(KNN_pred,Y_test)
print("Model Accuray of KNN Classifier :",Accuracy_KNN * 100)
print(border)


cm = confusion_matrix(Y_predlr,Y_test)
print("Confusion matrix  :")
print(cm)
print(border)


report= classification_report(Y_predlr,Y_test)
print("Classification Report :",report)
print(border)

data = ConfusionMatrixDisplay(confusion_matrix = cm , display_labels = lr_model.classes_)
data.plot()
plt.title("confusion matrix of Diabetes dataset")
plt.show()
print(border)

results = pd.DataFrame({
    "Actual " : Y_test.values,
    "Logistic_predicted" : Y_predlr
})

print(results.head())
results.to_csv("Model_predictions.csv",index = False)
print("Csv  File sucessfully saved")
