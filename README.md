# Onyo Challenge

# Description

This project is a challenge for a job opening at Onyo. It's a Zipcode API

Deployed app at Heroku: https://zipcodeapionyo.herokuapp.com/

# Installing

First step of installation is having Pipenv installed in your machine, if you doesn't have just use the below command:

``` $ pip install pipenv ```

Now after cloned the repository all you need to do is:

```
$ cd zipcodeapi/
$ pipenv install
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# Testing

To test the application use:

```$ python manage.py test```


# API documentation

This API works with 1 endpoint:

## Zipcode Endpoint
This endpoint works at the **/getzipcode/-zipcode-**. It uses a brazilian type of zipcode like this '30330-330', and returns the fields needed. And only accepts
POST method.

POST data:

/getzipcode/30330330

Status: 200 OK
```
{
    "cep": "30330330",
    "address": "Rua Campo Belo",
    "neighborhood": "São Pedro",
    "city": "Belo Horizonte",
    "state": "MG"
}
```
