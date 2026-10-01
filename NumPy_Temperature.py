import numpy as np

temperatures = np.array([28, 30, 29, 31, 32, 33, 30, 29, 28, 31])

print("Original Temperatures:", temperatures)

print("Temperatures for First 3 Days:", temperatures[:3])

print("Temperatures from Day 5 to Day 8:", temperatures[4:8])

print("Average Temperature:", np.mean(temperatures))
print("Maximum Temperature:", np.max(temperatures))
print("Minimum Temperature:", np.min(temperatures))
print("Total Temperature:", np.sum(temperatures))

temperatures = temperatures + 2

print("Modified Temperatures:", temperatures)
