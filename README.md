This project is created to perform Employee CRUD operations by Narasimha Rao 'thehumanlion1214@gmail.com'

clone the project from 'https://github.com/Nara1412-ppb/User_CRUD.git'

install the requirements using 'pip install -r requirements.txt'

for mysql database connection 'pip install mysqlclient-1.4.6-cp38-cp38-win_amd64.whl'

data base credintials are imported from the database.py file in Jala_dashboard folder

migrate the model tables using 'python manage.py makemigrations' and 'python manage.py migrate'

run the server in the local machine by 'python manage.py runserver'

the functionality of the API is checked in testing tools like postman using the below urls

1. fetching the all users. 

    'http://127.0.0.1:8000/Employee/Search/'  in 'GET' method 

2. fetch the unique user using email or mobile no.

    'http://127.0.0.1:8000/Employee/Search/'  in 'POST' method. use the body in json format.

    {
        "EmailId":"",
    }

    replace the "EmailId" with "MobileNo" or both
3. Creating the user.

    'http://127.0.0.1:8000/Employee/Create/' in 'POST' method. use the body in json format.


    {
    "FirstName": "",
    "LastName": "",
    "EmailId": "",
    "MobileNo": "",
    "password": ""
    } 

4. Updating the user.

    'http://127.0.0.1:8000/Employee/Update/' in 'PUT' method. use the body in json format.

    In this route email need to add for fetching the user but email and mobile no won't change beacause the email and mobile fields are unique ane read only fields.

    {
    "FirstName": "Narasimha",
    "LastName": "Rao",
    "EmailId": "thehumanlion1214@gmail.com",
    "MobileNo": "8186094547",
    "DOB": "2018-05-05",
    "Address": "Hyderabad",
    "Gender": "Male",
    "CountryName": "India",
    "CityName": "Hyderabad",
    "Skills": "Python"
    }

5.  Deleting the User.

    'http://127.0.0.1:8000/Employee/Delete/' in 'DELETE' method.use the body in json format.

    in this route email should be passed in the json formate to fetch and delete the user.

    {
        "EmailId": "thehumanlion1214@gmail.com"
    }


NOTE:-  No authentication is developed it is only for CRUD operstions.





