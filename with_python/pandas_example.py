from re import A
import pandas as pd
from sqlalchemy.types import String, Date, Numeric

from database import engine

df = pd.DataFrame(
    {
        "first_name": ["Verna", "Pamela", "Roman"],
        "last_name": ["Hardy", "Brown", "Andrew"],
        "school": [
            "Myers Middle School",
            "Anderson High School",
            "Anderson High School",
        ],
        "hire_date": ["2020-09-2", "2019-07-04", "2019-07-06"],
        "salary": [35000, 40000, 34000],
    }
)

schema = {
    "first_name": String,
    "last_name": String,
    "school": String,
    "hire_date": Date,
    "salary": Numeric,
}

create_table_cmd = """
    create table if not exists good_pandas_teachers (
        id bigserial,
        first_name varchar,
        last_name varchar,
        school varchar,
        hire_date date,
        salary numeric
    );
"""


# append to existing table
df.to_sql("teachers", engine, if_exists="append", index=False)

# append to existing table -- specify schema to be safe
df.to_sql("teachers", engine, if_exists="append", dtype=schema, index=False)

# use pandas to make table directly
# not reccomended for most cases because pandas cannot make a primary key
# also not reccomended because pandas guesses the datatypes -- better to use schema
df.to_sql("bad_pandas_teachers", engine, if_exists="replace", index=False)

# use pandas to make table directly
# not reccomended for most cases because pandas cannot make a primary key
df.to_sql(
    "better_pandas_teachers", engine, if_exists="replace", dtype=schema, index=False
)

# create the schema with sqlalchemy
engine.connect().exec_driver_sql(create_table_cmd)

# load the teachers
df.to_sql("good_pandas_teachers", engine, if_exists="append", index=False)

# grab a whole table with pandas -- better to use a query
print(pd.read_sql_table("teachers", engine))

# execute a query with pandas
print(
    pd.read_sql_query(
        """
    select
        concat(last_name, ', ', first_name) as name,
        salary
    from
        teachers
    where
        school = 'F.D. Roosevelt HS' 
    """,
        engine,
    )
)
