# Project Overview

Welcome to *Test project* 

This project is for test purpose.

## Technologies Used

- Django
- Django Rest Framework
- Django Djoser
 

## Getting Started

### Prerequisites

Latest Python installed on your machine.

 
### Installation

1.  Clone the repo in your machine by entering this command in your terminal: `git clone https://github.com/MTTasin/Test_for_techforing.git` Or you can download the repo from here: https://github.com/MTTasin/Test_for_techforing
2. Open the terminal the the directory where the repo is cloned.
3.  Create an environment folder here by following this commands by assuming env is the folder name: 
`python -m venv env`
4. Now activate the environment by entering this commands:
`env\Scripts\activate`
5. Now install all the dependencies for backend:
`pip install -r requirements.txt`
6. Now enter this commands for Database migration `python manage.py makemigrations` & `python manage.py migrate`
7. Now create a super user so that you can monitor the API making the changes by entering this command and adding the data `python manage.py createsuperuser`
8. Now run the backend server by entering: `python manage.py runserver`
9. If everything goes right you will see a link on the terminal something like this: **http://127.0.0.1:8000**
10. Now this will be your backend domain for your API testings. 

#### Use this link in postman or your frontend projects.

### You can check out the API documentation here: https://documenter.getpostman.com/view/39612988/2sAY52cKiU



## Things that is not included in this project.

- Email Verification
- Sending Email
- Separate permissions for each user role
- Frontend

## Things that is not as exact as the requirements.
- The link for all the APIs are not the same as the documentation.
like the link for login in this project is `{{base_url}}/api/jwt/create/` but the documentation link is `{{base_url}}/api/users/login/` almost all the links are different from the requirements.
But the workflow is the same.
