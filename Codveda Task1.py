import pandas as pd
df = pd.read_csv("churn-bigml-20.csv")
print(df.head())
print("Dataset Shape:", df.shape)
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

for column in numerical_columns:
    df[column].fillna(df[column].median(), inplace=True)

# Fill categorical columns with the mode
categorical_columns = df.select_dtypes(include=['object']).columns

for column in categorical_columns:
    df[column].fillna(df[column].mode()[0], inplace=True)

# Verify missing values have been handled
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize categorical variables
for column in categorical_columns:
    df[column] = df[column].str.strip()       # Remove extra spaces
    df[column] = df[column].str.title()       # Standardize capitalization

# Standardize date columns (if any exist)
date_columns = []

for column in date_columns:
    df[column] = pd.to_datetime(df[column])

# Display cleaned dataset information
print("\nCleaned Dataset Information:")
print(df.info())

# Save the cleaned dataset
df.to_csv("churn-bigml-20_cleaned.csv", index=False)

print("\nData cleaning and preprocessing completed successfully!")