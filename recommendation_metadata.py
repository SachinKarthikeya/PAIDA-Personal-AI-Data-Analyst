def extract_dataset_metadata(df, target_column):
    metadata = {}

    # Basic information
    metadata["num_samples"] = df.shape[0]
    metadata["num_features"] = df.shape[1] - 1
    metadata["target_column"] = target_column

    # Task Type
    if df[target_column].nunique() <= 20:
        metadata["task_type"] = "classification"
        metadata["num_classes"] = df[target_column].nunique()
        metadata["class_balance"] = (
            df[target_column].value_counts(normalize=True).to_dict()
        )
    else:
        metadata["task_type"] = "regression"

    # Feature Types
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()
    numerical = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    metadata["feature_types"] = {
        "categorical": len(categorical),
        "numerical": len(numerical),
    }

    metadata["missing_values_ratio"] = df.isnull().mean().mean()

    high_cardinality_features = [
        col for col in categorical if df[col].nunique() > 20
    ]
    metadata["high_cardinality_features"] = high_cardinality_features

    # Dataset Size Heuristic
    if metadata["num_samples"] < 5000:
        metadata["dataset_size"] = "small"
    elif metadata["num_samples"] < 100000:
        metadata["dataset_size"] = "medium"
    else:
        metadata["dataset_size"] = "large"

    return metadata