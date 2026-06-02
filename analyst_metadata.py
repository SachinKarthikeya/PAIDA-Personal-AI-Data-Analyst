import pandas as pd
import numpy as np

def extract_metadata(df):
    dataset = pd.DataFrame(df)

    analyst_metadata = {
        "columns": dataset.columns.tolist(),
        "shape": [int(x) for x in dataset.shape],
        "dtypes": dataset.dtypes.astype(str).to_dict(),
        "sample_records": dataset.head(5).to_dict(orient="records"),
        "statistical_summary": dataset.describe(include="all").fillna("").to_dict(),
        "missing_values": {
            k: int(v) for k, v in dataset.isnull().sum().to_dict().items()
        },
        "unique_values": {
            k: int(v) for k, v in dataset.nunique().to_dict().items()
        },
    }

    return analyst_metadata
