-- create the teachers table

create table teachers (
    id bigserial,
    first_name varchar,
    last_name varchar,
    school varchar,
    hire_date date,
    salary numeric
);