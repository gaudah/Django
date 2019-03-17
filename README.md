**Requirements**

1. *Python3.7.0*
2. *python-pip PIP: PIP3*
    - sudo apt-get install python-pip python-dev build-essential
    - sudo pip install --upgrade pip 
3. *postgresql-9.5.x*


**Getting started**
1. Clone this repo: git clone https://ipratik@bitbucket.org/ipratik/django-assignment-api.git

2. Change to the repo directory: cd django-assignment-api

3. Install dependencies with pip: sudo pip install -r requirement.txt

4. Run the app:  python manage.py runserver or  python3 manage.py runserver

5. Running on https://ipratik-heroku-idemoapp.herokuapp.com/

6.For migrations: 
   - python manage.py makemigrations or python3 manage.py makemigrations
   - python manage.py migrate or python3 manage.py migrate 


**Routes**
List of API is published on follwoing URL: https://ipratik-heroku-idemoapp.herokuapp.com/

API are divided into 4 sections:=
1.locations
   - GET /api/locations/ - Return all the user locations
   - GET /api/locations/{userId}/ - Get all locations by specific userId or by specific start and end date range
       - GET /api/locations/{userId}/ -  Get User wise locations details
       - GET /api/locations/{userId}/?search = query_string -  Search based on the start date and end date 
       where search parameter uses the format as YYYY-MM-DD
          Eg. /api/locations/2/?search={ \"startDate\": \"2018-10-17\",  \"endDate\": \"2018-10-20\"}"
       -  GET /api/locations/{userId}/?search = query_string - Search based on the start date only
       where search parameter uses the format as YYYY-MM-DD
          Eg. /api/locations/2/?search={ \"startDate\": \"2018-10-17\"}"
   - POST /api/locations/{userId}/ - Post the location details of specific userId
2.login
   - POST /api/login/ - login api of user
3. register
   - POST /api/register/ -  Post the user details 
4. users
   - GET /api/users/ - Return all the user details
   - GET /api/users/{id}/ - Get user details by id
   - PUT /api/users/{id}/ - Update user details by id
   
5. admin
   - https://id.heroku.com/login - login api of admin


**Database Schema**
1. Users:=
   Fields:
     - id - BigAutoField - primary_key=True, serialize=True, auto_created=True # Auto created id for user
     - username - CharField(max_length=50)
     - firstName - CharField(max_length=50)
     - middleName - CharField(max_length=50)
     - lastName - CharField(max_length=50)
     - email  - CharField(max_length=50) - unique=True # Should be unique
     - mobile  - CharField(max_length=15) - unique=True # Should be unique
     - password - CharField(max_length=100) - encoded using md5 
     - isSuperuser - BooleanField
     - isStaff - BooleanField
     - isUser - BooleanField
     - isActive - BooleanField
     - dateJoined - DateTimeField - auto_now_add=True
     - lastLogin - DateTimeField - null=True
     - createdAt - DateTimeField - auto_now_add=True
     - updatedAt - DateTimeField - auto_now_add=True
     
     
2. UsersLocation:=
    Fields:
    - id -  BigAutoField - primary_key=True, serialize=True, auto_created=True # Auto created id for user location  
    - userId - BigIntegerField
    - latitude - FloatField(max_length=21)
    - longitude - FloatField(max_length=21)
    -  area - TextField(null=False)
    - createdAt - DateTimeField - auto_now_add=True
    - updatedAt - DateTimeField - auto_now_add=True

