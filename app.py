import streamlit as st
import pandas as pd

from llm_agent import llm_query, recommendation_query
from toolbox import *
from model_recommendation import extract_dataset_metadata

st.title("🧠 PAIDA - Your Personal AI Data Analyst")
st.write("Upload your dataset and ask for the data analysis tasks required for your project.")

uploaded_file = st.file_uploader("Upload your Dataset in CSV, JSON or Excel format", type=["csv", "json", "xlsx"])
df = pd.DataFrame()

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    if "df" not in st.session_state:
        st.session_state["df"] = df.copy()

    st.success("Dataset uploaded successfully!")
    st.dataframe(st.session_state["df"].head()) 
    st.write(f"Shape: {st.session_state['df'].shape}")

    user_query = st.chat_input("Enter your required data analysis task:")

    if user_query:
        decision = llm_query(user_query)
        action = decision.get("action")

        df = st.session_state["df"]

        if action == "show_tail":
            st.dataframe(show_tail(df))

        elif action == "dataset_info":
            info = dataset_info(df)
            st.code(info)

        elif action == "statistical_summary":
            summary = statistical_summary(df)
            st.dataframe(summary)

        elif action == "feature_columns":
            features = feature_columns(df)
            st.write(features)

        elif action == "target_class_distribution":
            target_column = df.columns[-1] 
            distribution = target_class_distribution(df, target_column)
            st.dataframe(distribution)

        elif action == "missing_values":
            missing = missing_values(df)
            st.dataframe(missing)

        elif action == "remove_missing_values":
            missing_after = remove_missing_values(df)
            st.session_state["df"] = df
            st.dataframe(missing_after)

        elif action == "duplicate_values":
            duplicates = duplicate_values(df)
            st.write(f"Number of duplicate rows: {duplicates}")

        elif action == "remove_duplicates":
            df, removed_count = remove_duplicates(df)
            st.session_state["df"] = df
            st.write(f"Removed {removed_count} duplicate rows.")

        elif action == "remove_columns":
            column_names = decision.get("column_names", [])
            df, removed_cols, missing_cols = remove_columns(df, column_names)
            st.session_state["df"] = df
            st.write(f"Removed columns: {removed_cols}")
            if missing_cols:
                st.write(f"Columns not found in dataset: {missing_cols}")
        
        elif action == "correlation_heatmap":
            fig = correlation_heatmap(df)
            st.pyplot(fig)

        elif action == "outlier_detection":
            outliers = outlier_detection_iqr(df)
            st.dataframe(outliers)

        elif action == "min_max_scaling":
            feature_cols = df.select_dtypes(include="number").columns.tolist()
            df = min_max_scaling(df, feature_cols)
            st.session_state["df"] = df
            st.dataframe(df.head())

        elif action == "standard_scaling":
            feature_cols = df.select_dtypes(include="number").columns.tolist()
            df = standard_scaling(df, feature_cols)
            st.session_state["df"] = df
            st.dataframe(df.head())

        elif action == "label_encoding":
            categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
            df = label_encoding(df, categorical_cols)
            st.session_state["df"] = df
            st.dataframe(df.head())

        else:
            st.error("Invalid action.")

    st.subheader("⬇️ Download Modified Dataset")

    csv_dataset = st.session_state["df"].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv_dataset,
        file_name="modified_dataset.csv",
        mime="text/csv"
    )

    st.divider()
    st.subheader("🤖 ML / DL Model Recommendation")

    df = st.session_state["df"]

    target_column = df.columns[-1] 

    if st.button("Recommend Models"):
        dataset_metadata = extract_dataset_metadata(df, target_column)
            
        st.subheader("📊 Dataset Metadata")
        for key, value in dataset_metadata.items():
            st.write(f"**{key}**: {value}")

        with st.spinner("Analyzing dataset and recommending models..."):
            recommendations = recommendation_query(dataset_metadata)

        st.subheader("🤖 Recommended Models")
        if "recommended_models" in recommendations:
            for model in recommendations["recommended_models"]:
                st.markdown(f"**Model:** {model['model_name']}")
                st.markdown(f"**Reason:** {model['reason']}")
                st.markdown("---")
        else:
            st.error("Failed to generate model recommendations.")