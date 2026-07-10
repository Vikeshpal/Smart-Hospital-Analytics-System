def dataset_information(df):
    print("\nDataset Information:")
    print(df.info())


def statistical_summary(df):
    print("\nStatistical Summary:")
    print(df.describe())


def check_missing_values(df):
    print("\nMissing Values:")
    print(df.isnull().sum())


def check_duplicate_values(df):
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())