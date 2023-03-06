import numpy as np
import matplotlib.pyplot as plt

# create the dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# calculate the values needed for the regression line
n = np.size(x)
mean_x, mean_y = np.mean(x), np.mean(y)
SS_xy = np.sum(y*x - n*mean_y*mean_x)
SS_xx = np.sum(x*x - n*mean_x*mean_x)
beta_1 = SS_xy / SS_xx
beta_0 = mean_y - beta_1*mean_x

# plot the data points and the regression line
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, beta_0 + beta_1*x, color='red', label='Regression line')

# add title, labels, and legend to the plot
plt.title('Simple Linear Regression')
plt.xlabel('Independent variable')
plt.ylabel('Dependent variable')
plt.legend()

# show the plot
plt.show()
