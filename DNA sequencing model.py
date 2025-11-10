#

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

data_source = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/cpg_methylation_age_data.csv"
df = pd.read_csv(data_source, sep = ",")

x = df.drop(columns = ['Age'])
y = df['Age']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

linear_model_fs = LinearRegression()

rfe = RFE(estimator = linear_model_fs, n_features_to_select = 100, step = 10)

rfe.fit(x_train, y_train)

selected_features = x_train.columns[rfe.support_]

x_train_selected = x_train[selected_features]
x_test_selected = x_test[selected_features]

print(f"Selected Features: {selected_features}")

linear_model = LinearRegression()
linear_model.fit(x_train_selected, y_train)
y_linear_predict = linear_model.predict(x_test_selected)
linear_mse = mean_squared_error(y_test, y_linear_predict)


rf_model = RandomForestRegressor(n_estimators = 100, random_state = 42)
rf_model.fit(x_train_selected, y_train)
# initailly, I was getting a fit error because I equated the rf_model.fit = (x,y) instead of rf_model.fit(x,y)
y_rf_pred = rf_model.predict(x_test_selected)
rf_mse = mean_squared_error(y_test, y_rf_pred)

print(f"Random Forest Regression MSE with feature selection: {rf_mse} ")

print("Let's compare")
print(f"Linear model: {linear_mse}")
print(f"Random forest regressor: {rf_mse}")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

link = ("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/cpg_methylation_age_data.csv")

df2 = pd.read_csv(link, sep = ",")
print(df2.head())


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

logistic_model_fs = LogisticRegression(max_iter=1000)

# Apply RFE to select top 50 features
rfe = RFE(estimator=logistic_model_fs, n_features_to_select=50, step=10)

# just to note, Logistic regression doesn't deal with floats but guess whose dataframe is in float. Had to convert my training dataset below
# for my fit to work properly
x_train = x_train.astype(int)
y_train = y_train.astype(int)
y_test = y_test.astype(int)


rfe.fit(x_train, y_train)


# Selected features
selected_features = x_train.columns[rfe.support_]
x_train_selected = x_train[selected_features]
x_test_selected = x_test[selected_features]

print(f"Selected features: {selected_features}")

logistic_model = LogisticRegression(max_iter = 1000)
logistic_model.fit(x_train_selected, y_train)

y_log_pred = logistic_model.predict(x_test_selected).astype(int)


print("Logistic Regression Accuracy:", accuracy_score(y_test, y_log_pred))
print("Classification Report:\n", classification_report(y_test, y_log_pred))


ranf_model = RandomForestClassifier(n_estimators = 100, random_state = 42 )
ranf_model.fit(x_train_selected, y_train)
y_ranf_pred = ranf_model.predict(x_test_selected)

print("Evaluating accuracy score with random forest classifier:", accuracy_score(y_test, y_ranf_pred))
print("Evaluating classification report with random forest classifier:", classification_report(y_test, y_ranf_pred))


# the linear model has a lower mean squared error so it's better for this task
