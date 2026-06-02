# 📊 PAIDA - Personal AI Data Analyst

An AI based data analytics assistant which can:

1. Automate tasks like Data Cleaning, Visualization, Pre-processing, etc. required before building an ML model.
2. Give useful insights about the dataset by analyzing the dataset.
3. Recommend efficient ML/DL models based on the dataset's structure.

This project enhances the automation of data analytics by performing safe and deterministic task execution, efficient business analysis and model recommendations, avoiding human errors as well as LLM hallucinations.

## 🚀 Features

- **Llama3.2:1b / Llama 3.1:8b**: Analyzes the user task through Natural Language Processing
- **JSON**: Acts as a bridge between LLM and Python toolbox for structuring output formats
- **Python Toolbox**: Uses libraries like **Pandas**, **Numpy**, **Matplotlib**, **Seaborn** and **Scikit-learn** to perform required tasks
- **MySQL Database**: To store the modified dataset 
- **Streamlit**: As a visualistic and interactive dashboard
- Extracts dataset's metadata for model recommendations and business insights
- Users can download the modified dataset in CSV format
- Supports data input formats like **CSV**, **JSON** or **Excel**

## 📄 Workflow

The project mainly consists of three features available for the users:

1. Modify your Dataset

- User uploads a dataset in either of the supported formats
- Request for a task among EDA, Data Handling, Feature Engineering, Transformation and Scaling, etc. to be performed
- LLM understands the query given by the user and responds in JSON format
- The pre-written code in python executes the task and structures output according to the JSON format
- Displays the results in structured format 
- Lets the user download the final modified dataset in CSV format
- Allows the user to store the modified dataset in an SQL database in case of disaster recovery or during the use of automated pipelines

2. Know about your Dataset

- User uploads a dataset in either of the supported formats
- The dataset's details like Columns, Dimensions, Statistical Summary, Missing Value Count and Target Class Distribution are extracted in metadata format.
- The LLM understands the metadata to give useful insights like Key Patterns, Potential Data Quality Issues, Interesting Correlations and Recommendations to improve dataset's quality.

3. Recommend Models for your Dataset

- User uploads a dataset in either of the supported formats
- Python tool extracts the dataset's metadata 
- LLM analyzes the summary
- Recommends top 3 models with brief explanation in JSON
- Structured format is then displayed on the dashboard

## 📁 Versions
For this project, there are two versions which work separately:

**Version 1:**

- MySQL database integrated
- Original local Ollama model integrated
- Docker containerization and Render hosting not performed.

**Version 2:**

- No MySQL database integrated
- Changed the LLM from locally running Ollama model to API-based OpenAI model
- Containerized the project using Docker and hosted using Render

## 🧰 Tech Stack

- Frontend: Streamlit
- Backend: Python toolbox, JSON
- LLM: Llama 3.2:1b (via Ollama) / Llama3.1:8b (production)
- Database: MySQL
- Deployment: Docker & Render

## 📢 Future Enhancements

- Summarizing total tasks report along with model recommendations and exporting in PDF
- Auto generate train-test splits and model training pipelines after data preparation
- Downloading the trained models along with the metrics and loss reports
