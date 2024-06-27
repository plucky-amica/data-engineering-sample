import pandas as pd
from sqlalchemy import create_engine

def create_sample_data():
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [24, 27, 22, 32, 29],
        'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eva@example.com']
    }
    return pd.DataFrame(data)

def save_to_database(df, engine):
    df.to_sql('customers', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
    df = create_sample_data()
    save_to_database(df, engine)
    print("Data not saved to database")
