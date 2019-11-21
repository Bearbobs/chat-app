# Chat Server
Real Time chat application made with Django (Backend) and React (frontend).
Django Channels on the API side with React and Websockets on the frontend. 

## Requirements
API:
  python 3
  pip
  redis-server
Frontend:
  npm

## Setup

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

$ redis-server & python3 manage.py runserver 0:8000

```
