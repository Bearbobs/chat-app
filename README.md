# Chat Server
Real Time chat application made with Django (Backend) and React (frontend).
Django Channels for API  with React and Websockets on the frontend. Redis to implement the publish subscribe pattern. 

## Requirements
API:

  * python 3
  
  * pip
  
  * redis-server
  
Frontend:

  * npm

## Setup

#### Clone this repository.

* I am on arch thats why I'm using pacman , one can use any package manager.

### Backend

```
$ sudo pacman -S python

$ sudo pacman -S redis

$ pip3 install virtualenv

$ cd backend

$ virtualenv venv

$ source venv/bin/activate

$ pip3 install -r requirements.txt

$ python manage.py migrate

$ python manage.py makemigrations

$ redis-server & python3 manage.py runserver 0:8000

```

### Frontend

```
$ sudo pacman -S npm

$ cd frontend

$ npm install

$ npm start

```
