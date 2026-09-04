# Given X, Y and Z values
X = [12.1, 13.2, 15.6, 17.2, 18.8, 10.3, 11.7, 16.4]
Y = [48, 59, 32, 18, 41, 32, 31, 30]
Z = [101, 171, 112, 132, 140, 112, 151, 96]

# Number of observations
n = 0
for i in X:
    n = n + 1

# Calculate sum of X, Y and Z
sumX = 0
sumY = 0
sumZ = 0
for i in range(n):
    sumX = sumX + X[i]
    sumY = sumY + Y[i]
    sumZ = sumZ + Z[i]

# Calculate means
meanX = sumX / n
meanY = sumY / n
meanZ = sumZ / n
print("Mean X =", meanX)
print("Mean Y =", meanY)
print("Mean Z =", meanZ)

# Calculate deviations and sums of squares/products
sumX2 = 0
sumY2 = 0
sumZ2 = 0
sumXY = 0
sumXZ = 0
sumYZ = 0
for i in range(n):
    x = X[i] - meanX
    y = Y[i] - meanY
    z = Z[i] - meanZ
    sumX2 = sumX2 + x * x
    sumY2 = sumY2 + y * y
    sumZ2 = sumZ2 + z * z
    sumXY = sumXY + x * y
    sumXZ = sumXZ + x * z
    sumYZ = sumYZ + y * z

# Calculate variances and covariances
varX = sumX2 / (n-1)
varY = sumY2 / (n-1)
varZ = sumZ2 / (n-1)
cov_X_Y = sumXY / (n-1)
cov_X_Z = sumXZ / (n-1)
cov_Y_Z = sumYZ / (n-1)

# Covariance matrix
print("\nCovariance Matrix:")
print("[", varX, ",", cov_X_Y, ",", cov_X_Z, "]")
print("[", cov_X_Y, ",", varY, ",", cov_Y_Z, "]")
print("[", cov_X_Z, ",", cov_Y_Z, ",", varZ, "]")