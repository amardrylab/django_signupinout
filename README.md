# Creating a class based view (Sign up in and out)  using Django server on GCP

### This example simply show the use of CreateView class

## 1) Clone the ansible script on your local machine

git clone https://github.com/amardrylab/ansible_djangoserver3.git

## 2) Change directory and start the ansible-playbook

- cd ansible_djangoserver3
- ansible-playbook instance_create.yml

## 3) SSH to your created machine

ssh www.drylab.in

## 4) Create your virtual environment

virtualenv myproject

## 5) Install git software

- sudo apt-get install git

## 6) Clone the django scripts

 git clone https://github.com/amardrylab/django_signupinout.git


## 7) Copy the required files in proper location

mv django_signupinout/*  myproject

## 8) Enter your virtual environment

- source myproject/bin/activate
- cd myproject

## 9) Install the required softwares in the local environment

- pip install django

## 10) Make migrations and migrate

- ./manage.py makemigrations
- ./manage.py migrate

## 11) Restart the services

- sudo service nginx restart
- sudo service uwsgi restart
