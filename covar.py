# Given Heights And Weights
h = [1.70, 1.62, 1.52, 1.85, 1.91, 1.42]
wt = [72, 64, 84, 80, 72, 70]

# Number of observations
n = 0

for i in h:
    n = n + 1

# Calculate sum of height and weight
sumH = 0
sumWt = 0

for i in range(n):
    sumH = sumH + h[i]
    sumWt = sumWt + wt[i]

# Calculate means
meanH = sumH / n
meanWt = sumWt / n

print("Mean Height =", meanH)
print("Mean Weight =", meanWt)

# Calculate deviations
sumX2 = 0
sumY2 = 0
sumXY = 0

for i in range(n):

    x = h[i] - meanH
    y = wt[i] - meanWt

    sumX2 = sumX2 + x * x
    sumY2 = sumY2 + y * y
    sumXY = sumXY + x * y

# Calculate variances and covariance
varH = sumX2 / (n-1)
varWt = sumY2 / (n-1)
cov_H_Wt = sumXY / (n-1)

# Covariance matrix
print("\nCovariance Matrix:")

print("[", varH, ",", cov_H_Wt, "]")
print("[", cov_H_Wt, ",", varWt, "]")