import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

print("Original Dataset:")
print(df.head())


print("\nDataset Information:")
df.info()

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)


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


for col in df.select_dtypes(include=["object", "category"]).columns:
    if df[col].isnull().any() and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


print("\nSummary Statistics:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include="object"))

for col in df.select_dtypes(include=np.number).columns:
    values = df[col].dropna().to_numpy()

    if len(values) > 0:
        print(f"\nStatistics for {col}:")
        print("Mean:", np.mean(values))
        print("Median:", np.median(values))
        print("Minimum:", np.min(values))
        print("Maximum:", np.max(values))
        print("Standard Deviation:", np.std(values))


if "Churn" in df.columns:
    churn_counts = df["Churn"].value_counts()

    print("\nCustomer Churn Count:")
    print(churn_counts)

    print("\nCustomer Churn Percentage:")
    print(df["Churn"].value_counts(normalize=True) * 100)

  
    churn_counts.plot(kind="bar")

    plt.title("Customer Churn Analysis")
    plt.xlabel("Churn Status")
    plt.ylabel("Number of Customers")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


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


if "Tenure" in df.columns and "Churn" in df.columns:
    df.boxplot(column="Tenure", by="Churn")

    plt.title("Customer Tenure by Churn Status")
    plt.suptitle("")
    plt.xlabel("Churn Status")
    plt.ylabel("Tenure")
    plt.tight_layout()
    plt.show()


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
