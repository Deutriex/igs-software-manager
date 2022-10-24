# Installation- Install Anaconda3- Run this following command on the Anaconda Prompt to get all dependencies and have everything installed:`conda env create -f igs_software_manager.yml`The `igs_software_manager.yml` file is in the same folder as this `readme.md` It will create a new `django_dev` virtual env with all the stuff needed to run the projectActivate it by typing `conda activate django_dev`Start the server by running `python manage.py runserver`. You should be presented to the employee list.## Software used for building this project:- Python 3.7.0- SQLite 3.39.3- Django 3.2.16- Django REST framework 3.14.0# Super user data- Login: `IGS_admin`- Password: `IGS_2022`# API documentation## Employees### List employeesCommand (WSL, bash, terminal): `curl -H "Content-Type: application/javascript" http://localhost:8000/employee/`List all employees from the database### Add a new employeeCommand (WSL, bash, terminal): `curl -X "POST" -d "name=John%20Doe&email=john.doe@igs-software.com.br&department=2" http://localhost:8000/employee/create/`The keys follow the Employee model in a GET-like, URL-encoded format for the `-d`parameter, but it receives a POST request instead.### Delete an existing employee by idCommand (WSL, bash, terminal): `curl -H "Content-Type: application/javascript" -X "DELETE" http://localhost:8000/employee/3/delete/`## Department### List departmentsCommand (WSL, bash, terminal): `curl -H "Content-Type: application/javascript" http://localhost:8000/department/`List all the departments from the database and their respective IDs.### Add a new departmentCommand (WSL, bash, terminal): `curl -X "POST" -d "name=New%20departament" http://localhost:8000/department/create/`Create a new deparment with a new id auto-generated by Django/SQLiteIt can be used as a reference for future employees.### Delete an existing department by idNotice: This command will only work if there is nobody under the department.Otherwise the department won't be removed and a JSON with `{"success": false}` willbe returned instead.Command (WSL, bash, terminal): `curl -H "Content-Type: application/javascript" -X "DELETE" http://localhost:8000/department/5/delete/`