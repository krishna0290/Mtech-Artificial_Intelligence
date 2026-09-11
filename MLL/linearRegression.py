import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV (no pandas needed, just numpy)
data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
X = data[:, 0]
y = data[:, 1]

n = len(X)

# ---- Manual Linear Regression (Least Squares) ----
# Formula for slope (m) and intercept (b) of y = m*x + b:
#   m = ( n*sum(X*y) - sum(X)*sum(y) ) / ( n*sum(X^2) - (sum(X))^2 )
#   b = ( sum(y) - m*sum(X) ) / n

sum_x = np.sum(X)
sum_y = np.sum(y)
sum_xy = np.sum(X * y)
sum_x2 = np.sum(X ** 2)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_y - m * sum_x) / n

print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")

# ---- Predictions ----
y_pred = m * X + b

# ---- R² score (manual) ----
ss_res = np.sum((y - y_pred) ** 2)       # residual sum of squares
ss_tot = np.sum((y - np.mean(y)) ** 2)   # total sum of squares
r2 = 1 - (ss_res / ss_tot)
print(f"R² score: {r2:.4f}")

# ---- Plot ----
plt.scatter(X, y, color='blue', alpha=0.6, label='Data points')
sort_idx = np.argsort(X)
plt.plot(X[sort_idx], y_pred[sort_idx], color='red', linewidth=2, label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression from Scratch (No sklearn)')
plt.legend()
plt.show()

# ---- Predict new value ----
new_X = 7.5
prediction = m * new_X + b
print(f"\nPrediction for X=7.5: {prediction:.4f}")