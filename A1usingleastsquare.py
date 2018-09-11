
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('x03.csv')
data.head()

X = data['Age'].values
Y = data['Blood pressure'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)


n = len(X)

numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

print(b1, b0)
max_x = np.max(X) + 100
min_x = np.min(X) 

# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Age')
plt.ylabel('Blood pressure')
plt.legend()
plt.show()
