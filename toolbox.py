import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

def show_tail(df, n=5):
    return df.tail(n)

def dataset_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    buffer.close()
    return info_str

def statistical_summary(df):
    return df.describe()

def feature_columns(df):
    return df.columns.tolist()

def target_class_distribution(df, target_column):
    return df[target_column].value_counts()

def missing_values(df):
    return df.isnull().sum()

def remove_missing_values(df):
    df.dropna(inplace=True)
    return df.isnull().sum()

def duplicate_values(df):
    return df.duplicated().sum()

def remove_duplicates(df):
    before = df.shape[0]    
    df = df.drop_duplicates()
    after = df.shape[0]
    return df, before - after

def remove_columns(df, column_names):
    existing_columns = [col for col in column_names if col in df.columns]
    missing_columns = list(set(column_names) - set(existing_columns))

    df = df.drop(columns=existing_columns)
    return df, existing_columns, missing_columns

def correlation_heatmap(df):
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='Blues')
    fig = plt.gcf()
    return fig

def outlier_detection_iqr(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df < lower_bound) | (df > upper_bound)]
    return outliers

def min_max_scaling(df, feature_columns):   
    scaler = MinMaxScaler()
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    return df

def standard_scaling(df, feature_columns):
    scaler = StandardScaler()
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    return df

def label_encoding(df, categorical_columns):
    encoder = LabelEncoder()
    for col in categorical_columns:
        if col in df.columns:
            df[col] = encoder.fit_transform(df[col].astype(str))
    return df