import statistics

# Define a dataset
data = [5, 7, 11, 2, 10, 9, 6, 3, 5, 7]

# Compute the mean of the dataset
mean = sum(data) / len(data)
print("Mean:", mean)

# Compute the median of the dataset
median = statistics.median(data)
print("Median:", median)

# Compute the mode of the dataset
mode = statistics.mode(data)
print("Mode:", mode)

# Compute the variance of the dataset
variance = statistics.variance(data)
print("Variance:", variance)

# Compute the standard deviation of the dataset
std_dev = statistics.stdev(data)
print("Standard Deviation:", std_dev)
