-- insert a single teacher
insert into teachers (first_name, last_name, school, hire_date, salary)
values ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200);

-- insert a batch of teachers
insert into teachers (first_name, last_name, school, hire_date, salary)
values ('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
       ('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
       ('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
       ('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
       ('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);

-- update Betty's salary
update
	teachers
set
	salary = 50000
where
	first_name = 'Betty'
	and last_name = 'Diaz';

-- update Samantha's salary to the max salary
update
	teachers
set
	salary = (
	select
		max(salary)
	from
		teachers)
where
	first_name = 'Samantha'
	and last_name = 'Bush';

-- update to give everyone at Myers Middle School a $10000 raise
update
	teachers as t_new
set
	salary = (
	select
		salary + 10000 as salary
	from
		teachers t_old
	where
		t_new.first_name = t_old.first_name)
where
	school = 'Myers Middle School';

-- delete Samuel's entry because he quit
delete
from
	teachers
where
	first_name = 'Samuel'
	and last_name = 'Cole';