# Farhan-Todo

## Introduction 
Farhan to-do is todo app that will help you to manage your daily tasks.

## Features
<ul>
  <li> User Registration </li>
  <li> Add todo tasks </li>
  <li> Complete the todo task </li>
 </ul>
 
# Technology used
 
 <ul>
  <li> Django v-3.0.7 </li>
  <li> Postgres-sql </li>
 </ul>

## Usuage

### Clone Repository

Copy Paste the following commands to clone the repo

```bash
    git clone https://github.com/FarhanKhan1911/Farhan-Todo
```
Go inside the directory and install the module from requirements.txt

```bash
  pip install -r requirements.txt
 ```
 
 Then make the migrations and then migrate the database
 
 ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
  
  Create the superuser 
  
  ```bash
    python manage.py createsuperuser
  ```
  
  Now run the django server
  
  ```bash
    python manage.py runserver
  ````
  
  
  Now you goto localhost:8000 to see the website
  
  ```bash
      http://127.0.0.1:8000/
  ```

# Live Website
<h4> URL:- https://farhan-todo.herokuapp.com/ </h4>
