import pandas as pd

def extract_metadata(df):
    dataset = pd.DataFrame(df)

    analyst_metadata = {
        "columns": dataset.columns.tolist(),
        "shape": dataset.shape,
        "dtypes": dataset.dtypes.astype(str).to_dict(),
        "statistical_summary": dataset.describe().to_dict(),
        "missing_values": dataset.isnull().sum().to_dict(),
        "duplicate_values": dataset.duplicated().sum()
    }

    return analyst_metadata
