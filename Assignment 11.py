import pandas as pd
import numpy as np

numbers = pd.Series(np.random.randint(1, 101, 10),
                    index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])

print("Series:")
print(numbers)

print("\nFirst element using iloc:")
print(numbers.iloc[0])

print("\nElement with label 'C' using loc:")
print(numbers.loc["C"])

print("\nFirst three elements:")
print(numbers.iloc[0:3])

print("\nValues greater than 50:")
print(numbers[numbers > 50])

print("\nValues between 30 and 80:")
print(numbers[(numbers >= 30) & (numbers <= 80)])

print("\nMean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())
