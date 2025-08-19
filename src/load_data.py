import pandas as pd

def load_dataset(filepath):
    """
    Load the dataset and perform initial inspection.
    Returns the loaded DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def display_basic_info(df):
    """Display basic information about the dataset."""
    display(df.head(5))
    display(df.tail())
    print("Number of rows and columns:", df.shape)
    print("\nData types of each column:")
    df.info()
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("\nPercentage of missing values per column:")
    print(df.isnull().sum() / df.shape[0] * 100)

def convert_datetime(df, datetime_col='Datetime'):
    """Convert the datetime column to datetime objects."""
    df[datetime_col] = pd.to_datetime(df[datetime_col])
    return df

def display_unique_value_info(df, id_col='ID', datetime_col='Datetime'):
    """Display information about uniqueness of ID and Datetime columns."""
    num_unique_ids = df[id_col].nunique()
    total_rows = df.shape[0]
    print(f"Number of unique IDs: {num_unique_ids}")
    print(f"Total number of rows: {total_rows}")
    if num_unique_ids == total_rows:
        print("The 'ID' column contains unique values.")
    else:
        print("The 'ID' column does not contain unique values.")

    num_unique_datetimes = df[datetime_col].nunique()
    print(f"Number of unique Datetime values: {num_unique_datetimes}")
    print(f"Total number of rows: {total_rows}")
    if num_unique_datetimes == total_rows:
        print("The 'Datetime' column contains unique values.")
    else:
        print("The 'Datetime' column does not contain unique values.")

    # Display unique values for non-numerical columns
    non_numerical_cols = df.select_dtypes(include='object').columns
    for col in non_numerical_cols:
        print(f"\nUnique values in column '{col}':")
        print(df[col].value_counts())

if __name__ == "__main__":
    # Example usage
    filepath = '/content/dataset.csv'
    df = load_dataset(filepath)
    display_basic_info(df)
    df = convert_datetime(df)
    display(df.dtypes)
    display_unique_value_info(df)
