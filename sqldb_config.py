from sqlalchemy import create_engine

def get_engine():
    username = ""
    password = ""
    host = ""
    port = ""
    database = "paida_sql_database"

    engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
    return engine

def save_dataset_to_db(df, table_name):
    engine = get_engine()
    
    df.columns = df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.lower()

    df.to_sql(
        name = table_name,
        con = engine,
        if_exists = "replace",
        index = False
    )