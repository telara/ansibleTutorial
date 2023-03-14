import numpy as np
import matplotlib.pyplot as plt

# Results of stress test
results = [920, 950, 1000, 1140]

# Create histogram
hist, edges = np.histogram(results, bins=10)

# Plot histogram
plt.hist(results, bins=edges)
plt.title('Stress Test Results')
plt.xlabel('Requests per second')
plt.ylabel('Frequency')
plt.show()
