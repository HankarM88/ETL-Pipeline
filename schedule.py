from airflow import DAG
from airflow.operators.python import PythonOperator 
from datetime import datetime
from etl import extract, transform, load

FILE_PATH = "./data/reviews.csv"
# Import ETL functions from etl module to run the pipeline
 
def pipeline():
    # EXTRACT
    df = extract(FILE_PATH)
    # TRANSFORM
    transformed_df = transform(df)
    # LOAD
    load(transformed_df)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 13),
    'retries': 1 }

# Define the DAG
dag = DAG(
    'etl_pipeline',
    default_args = default_args,
    schedule = '@daily',  # Runs daily at 10 AM
    )

# Define tasks
etl_operator = PythonOperator(
    task_id = 'trigger_pipeline',
    python_callable = pipeline,
    dag = dag )

print("Tasks are Sucessefully Scheduled!")
