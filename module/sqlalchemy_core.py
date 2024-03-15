from sqlalchemy import create_engine, text
import yaml
'''
SQLAlchemy Core:

SQLAlchemy Core is a low-level SQL toolkit.
- It provides a set of Python functions and classes for building SQL statements and 
    interacting with databases using raw SQL.
- You work directly with SQL constructs like tables, columns, and expressions.
- It offers more control over the SQL generated, making it suitable for complex queries 
    and database-specific operations.
- SQLAlchemy Core does not involve creating Python classes that map to database tables, 
    as it operates at a lower level.
'''

with open('b_yaml_test.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

user = config['postgres']['user']
password = config['postgres']['password']
hostname = config['postgres']['host']
database_name = config['postgres']['database']


connection_str = f'postgresql://{user}:{password}@{hostname}/{database_name}'


try:
    engine = create_engine(connection_str)
    connection = engine.connect()
    
    result = connection.execute(text('SELECT * FROM employee'))
    for row in result:
        print(row)
    print(result)
    # print("connection successfull.")

except:
    print(f"Error")
