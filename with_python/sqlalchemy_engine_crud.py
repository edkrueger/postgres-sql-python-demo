from database import engine


def create_table():

    create_table_cmd = """
        create table if not exists sqlalchemy_teachers (
            id bigserial,
            first_name varchar,
            last_name varchar,
            school varchar,
            hire_date date,
            salary numeric
        );
    """

    with engine.connect(create_table_cmd) as connection:
        connection.exec_driver_sql(create_table_cmd)


def insert_one_dict_params(teacher):
    """Takes a teacher as a dict. Uses one dict as parameters to insert into sqlalchemy_teachers."""

    insert_template = """
        insert into sqlalchemy_teachers (first_name, last_name, school, hire_date, salary)
        values (%(first_name)s, %(last_name)s, %(school)s, %(hire_date)s, %(salary)s);
    """

    with engine.connect() as connection:
        connection.exec_driver_sql(insert_template, teacher)


def insert_many_dict_params(teachers):
    """Takes a list of teachers as a dicts. Uses a list of dicts as parameters to insert into sqlalchemy_teachers."""

    insert_template = """
        insert into sqlalchemy_teachers (first_name, last_name, school, hire_date, salary)
        values (%(first_name)s, %(last_name)s, %(school)s, %(hire_date)s, %(salary)s);
    """

    with engine.connect() as connection:
        connection.exec_driver_sql(insert_template, teachers)


if __name__ == "__main__":

    teachers = [
        {
            "first_name": "Verna",
            "last_name": "Hardy",
            "school": "Myers Middle School",
            "hire_date": "2020-09-2",
            "salary": 35000,
        },
        {
            "first_name": "Pamela",
            "last_name": "Brown",
            "school": "Anderson High School",
            "hire_date": "2019-07-04",
            "salary": 40000,
        },
        {
            "first_name": "Roman",
            "last_name": "Andrew",
            "school": "Anderson High School",
            "hire_date": "2019-07-06",
            "salary": 34000,
        },
    ]

    create_table()

    insert_one_dict_params(teachers[1])
    insert_many_dict_params(teachers[2:])
