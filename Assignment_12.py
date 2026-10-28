import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("customer_churn.csv")

print("Original Dataset:")
print(df.head())

# Step 2: Understand the dataset
print("\nDataset Information:")
df.info()

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Step 3: Check for missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 4: Remove duplicate records
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

# Step 5: Handle missing numerical values
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].mean())

if "MonthlyCharges" in df.columns:
    df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
        df["MonthlyCharges"].mean()
    )

if "Tenure" in df.columns:
    df["Tenure"] = df["Tenure"].fillna(
        df["Tenure"].median()
    )

# Step 6: Handle missing categorical values
for col in df.select_dtypes(include=["object", "category"]).columns:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Step 7: Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include="object"))

# Step 8: Calculate statistics using NumPy
for col in df.select_dtypes(include=np.number).columns:
    values = df[col].dropna().to_numpy()

    if len(values) > 0:
        print(f"\nStatistics for {col}:")
        print("Mean:", np.mean(values))
        print("Median:", np.median(values))
        print("Minimum:", np.min(values))
        print("Maximum:", np.max(values))
        print("Standard Deviation:", np.std(values))

# Step 9: Analyze customer churn
if "Churn" in df.columns:
    churn_counts = df["Churn"].value_counts()

    print("\nCustomer Churn Count:")
    print(churn_counts)

    print("\nCustomer Churn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)

    # Bar chart of customer churn
    churn_counts.plot(kind="bar")

    plt.title("Customer Churn Analysis")
    plt.xlabel("Churn Status")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Step 10: Visualize numerical data
if "Age" in df.columns:
    plt.hist(df["Age"].dropna(), bins=10)

    plt.title("Distribution of Customer Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

if "MonthlyCharges" in df.columns:
    plt.hist(df["MonthlyCharges"].dropna(), bins=10)

    plt.title("Distribution of Monthly Charges")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Step 11: Compare tenure with churn
if "Tenure" in df.columns and "Churn" in df.columns:
    df.boxplot(column="Tenure", by="Churn")

    plt.title("Customer Tenure by Churn Status")
    plt.suptitle("")
    plt.xlabel("Churn Status")
    plt.ylabel("Tenure")
    plt.tight_layout()
    plt.show()

# Step 12: Analyze correlations
numeric_df = df.select_dtypes(include=np.number)

if len(numeric_df.columns) >= 2:
    correlation = numeric_df.corr()

    print("\nCorrelation Matrix:")
    print(correlation)

    plt.imshow(correlation, interpolation="nearest")
    plt.colorbar()

    plt.xticks(
        range(len(correlation.columns)),
        correlation.columns,
        rotation=45,
        ha="right"
    )
    plt.yticks(
        range(len(correlation.columns)),
        correlation.columns
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# Step 13: Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

print("\nEDA Completed Successfully!")
