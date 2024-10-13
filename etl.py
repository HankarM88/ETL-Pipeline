import pandas as pd
from pymysql import connect
from preprocessing import clean, preprocess 
from sqlalchemy import create_engine
# design an ETL Pipeline that extract data from CSV file and ingest it into a MySQL database
# function 
def extract(file_path: str):
    
    """" Extract data from a local csv file"""
    df = pd.read_csv(file_path)
    print("Data Extracted")
    return df 


def transform(df):
    """" Transfrom data: Cleaning and Preprocessing """
    # clean and prepocess 
    preprocessed_df = df.copy()
    preprocessed_df['Preprocessed_review'] = df['Review'].apply(clean).apply(preprocess)
    print("Data Transformed")
    return preprocessed_df 

def load(df) -> None:
    """ Load Data into MySQL"""
    # Define MySQL database connection parameters
    user = 'hk'
    password = 'momokar88'
    host = 'localhost'
    port = 3306
    db = 'british_airways'
    
    # Create SQLAlchemy engine to connect to MySQL
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
    try:
        # Save DataFrame to MySQL (replace 'your_table_name' with your actual table name)
        df.to_sql('reviews', con=engine, if_exists='replace', index=False)
        print("Data saved to MySQL database.")

    except Exception as e:
        print(e)

# Test the pipeline
if __name__ == "__main__":
    df = extract("data/reviews.csv")
    df2 = transform(df)
    load(df2)






