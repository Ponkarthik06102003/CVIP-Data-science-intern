import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'data.csv' with your dataset file)
data = pd.read_csv('data.csv')

# Define the required features
required_features = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean",
                     "compactness_mean", "concavity_mean", "concave points_mean", "symmetry_mean",
                     "fractal_dimension_mean", "radius_se", "texture_se"]

# Filter the dataset to include only the required features
data = data[["diagnosis"] + required_features]

# Split the data into features (X) and target (y)
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Data preprocessing
scaler = StandardScaler()
imputer = SimpleImputer(strategy='mean')

X_train = imputer.fit_transform(X_train)
X_train = scaler.fit_transform(X_train)
X_test = imputer.transform(X_test)
X_test = scaler.transform(X_test)

# Train a machine learning model (Random Forest, for example)
model = RandomForestClassifier()
model.fit(X_train, y_train)


# Function to predict breast cancer based on user input
def predict_breast_cancer(new_data_point):
    # Data preprocessing for user input
    new_data_point = imputer.transform(new_data_point)
    new_data_point = scaler.transform(new_data_point)

    # Make a prediction
    prediction = model.predict(new_data_point)

    return prediction

print(" *********Please Enter the data as seen from the pathology report*********** ")
print("                                                                             ")

# Get user input for the required features
user_input = {}
for feature in required_features:
    user_input[feature] = float(input(f"Enter the value for '{feature}': "))

new_data_point = pd.DataFrame(user_input, index=[0])

# Predict breast cancer
result = predict_breast_cancer(new_data_point)

# Display the result to the user
if result[0] == 'M':
    print("The tumor is predicted as malignant.")
else:
    print("The tumor is predicted as benign.")

# Evaluate the model's performance and create a confusion matrix
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Display classification report
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)
print("**********PLEASE NOTE : This is only a prediction Generated using Past Datas Of Patients*************")

