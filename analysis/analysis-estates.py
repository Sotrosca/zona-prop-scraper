import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

data_path = './data/data-16-08-2021_214633.csv'

df = pd.read_csv(data_path)
df = df[df['badge'] == '$']
df.dropna(subset = ['Area'], inplace=True)
df.dropna(subset = ['prize'], inplace=True)

X = df.loc[:, 'Area'].values.reshape(-1, 1)
Y = df.loc[:,'prize'].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)

Y_pred = linear_regressor.predict(X)

mlpRegressor = MLPRegressor(
    hidden_layer_sizes=[20, 20, 20],
    activation='logistic',
    max_iter=2000,
    solver='adam',
    batch_size=5,
    learning_rate_init = 0.001,
    learning_rate = 'adaptive',
    shuffle=True,
    early_stopping=True,
    tol = 1e-10,
    n_iter_no_change=20)

X_mean = np.mean(X)
X_std = np.std(X)

Y_mean = np.mean(Y)
Y_std = np.std(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

X_train_rescaled = (X_train - X_mean) / X_std
Y_train_rescaled = (Y_train - Y_mean) / Y_std

X_test_rescaled = (X_test - X_mean) / X_std
Y_test_rescaled = (Y_test - Y_mean) / Y_std

mlpRegressor.fit(X_train_rescaled, Y_train_rescaled)

mlp_loss = mlpRegressor.loss_

mlp_test_loss = mlpRegressor.score(X_test_rescaled, Y_test_rescaled)

print('Loss: ' + str(mlp_loss))
print('Test loss: ' + str(mlp_test_loss))

#area_range = range(int(np.min(X)), int(np.max(X)) + 1)

prize_predict = []

area_linspace = np.linspace(int(np.min(X)), int(np.max(X)) + 1, 1000)

for i in area_linspace:
    if i % 200 == 0:
        print(i)
    Y_mlp_pred = mlpRegressor.predict([[(i - X_mean) / X_std]])

    y_mlp_pred_rescaled = Y_mlp_pred * Y_std + Y_mean

    prize_predict.append(y_mlp_pred_rescaled)

prize_predict = np.array(prize_predict)

plt.scatter(X_train, Y_train, marker='.')
plt.scatter(X_test, Y_test, marker='.', color='red')
plt.plot(X, Y_pred, color='red')
plt.plot(area_linspace, prize_predict, color='black')
plt.show()

best_estates = df[df['prize'].values.reshape(-1, 1) < linear_regressor.predict(df['Area'].values.reshape(-1, 1))]