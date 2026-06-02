import pandas as pd

def extract_metadata(df):
    dataset = pd.DataFrame(df)

    analyst_metadata = {
        "columns": dataset.columns.tolist(),
        "shape": dataset.shape,
        "statistical_summary": dataset.describe(include="all").to_dict(),
        "missing_values": dataset.isnull().sum().to_dict(),
        "target_class_distribution": dataset[dataset.columns[-1]].value_counts().to_dict()  
    }

    return analyst_metadata