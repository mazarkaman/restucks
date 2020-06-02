

# Django Restbucks Challenage

## Installation

in order to install and run this project go to project directory and run this commands in your terminal:

```sh
 docker-compose -f ./docker-compose-prod.yml up -d --build
```

## Admin panel
In order to go to admin panel run this command:

```sh
docker-compose -f ./docker-compose-prod.yml run webservice sh -c "python manage.py createsuperuser"
```

and go to this url:
 [http://127.0.0.1:800/admin](http://127.0.0.1:800/admin)
 and enter your account info


## Run tests

```sh
docker-compose -f ./docker-compose-prod.yml run webservice sh -c "python manage.py test"
```

## Api documentation
 

Open [http://127.0.0.1:800/swagger](http://127.0.0.1:800/swagger) in browser


