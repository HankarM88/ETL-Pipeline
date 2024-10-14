# Building An offline ETL Pipeline 
In this pipeline, we  implement an offline simple ETL (Extract, Transform, Load) pipeline using a CSV file as the data source. The pipeline performs data extraction, applies necessary transformations, and loads the transformed data into MySQL database.

### Features
- **Data Extraction**: Reads data from a CSV file.
- **Data Transformation**: Applies a series of transformations to clean and prepare the data.
- **Data Loading**: Ingests the transformed data into MySQL database. 

### Requirements  
- Pandas
- SQLalchemy
- airflow
- nltk

### Installation 
1. Clone the Repository:<br>
```git clone https://github.com/HankarM88/ETL-Pipeline```
3. Install Dependencies:<br>
```pip install -r requirements.txt```

### Usage
1. Run ETL Pipeline:<br> 
```python3 etl.py```
2. Execution:<br>
- Load data from the data/reviews.csv file.
- Apply the transformations(cleaning and preprocessing).
- Ingest processed data into  MySQL database.

