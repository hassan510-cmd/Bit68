# Bit68
> Python Requirements
## 1- clone this repo
## 2- cd into repo root folder
## 3- pip install -r requirements.txt

> Database Requirements
## 1- create new database with the following credential 
            'NAME': 'Bit68',
            'HOST': "localhost",
            'USER': 'postgres',
            'PASSWORD': '691999',
            'PORT': '5432'
> Migration Requirements
## 1- start postgres service by run this 
      service postgres start 
## 2- cd into repo root folder
## 3- active you venv (if you have)
## 4- run this commands 
    python3 manage.py makemigrations
    python3 manage.py migrate
<hr/>

# Endpoints

## Seller

### get all users GET

```diff
+ http://127.0.0.1:8000/user/register/
```
> response
```json
[
    {
        "username": "admin",
        "password": "pbkdf2_sha256$320000$Bhf503wIWT4EhqvwYX56xA$20iLsvSCT1nNIqbTUqI27P+Ds871x3v0+U7mxAk/Ou0=",
        "email": "admin@admin.com"
    },
    {
        "username": "gihyjukiby",
        "password": "Vero ducimus nostru",
        "email": "dezo@mailinator.com"
    },
    {
        "username": "megynupi",
        "password": "pbkdf2_sha256$320000$Zf6bN7OqBxfZcSrrSisIG7$SjopuaBrJyFNadD6S+6QQEJ14KRaDFIsDujcGcoJBdA=",
        "email": "xaxulujaxo@mailinator.com"
    },
    {
        "username": "zehiqejef",
        "password": "pbkdf2_sha256$320000$qK52DICq0Sj5ofWIoqwQgn$KS5aHqrah5oQq8urs2JNZT234ZAuu+Vhc9H7qGaKUQU=",
        "email": "myfymecahy@mailinator.com"
    }
]
```

### register POST

```diff
! http://127.0.0.1:8000/user/register/
```
> body
```json
{
    "username":"hassan",
    "email":"hassan@gmail.com",
    "password":"2020",
    "confirm_password":"2020"
}
```

> response
```json
{
    "user": {
        "username": "hassan",
        "password": "pbkdf2_sha256$320000$KGMmPoex5G25Fe0uvykTTt$JwUwTI4nGRG790qJ63wxKSzfnACrUnQ5XvthZ9BjtGU=",
        "email": "hassan@gmail.com"
    },
    "token": "e849cca20ea81bf7bee5dfdc047179db544c44c9"
}
```


### login POST

```diff
! http://127.0.0.1:8000/user/login
```
> body
```json
{
    "username": "admin@admin.com",
    "password": "admin"
}
```

> response
```json
{
    "token": "eb7c0e9789f2166697bcc6b43ab8deb447acddf3"
}
```

## Product

### get all products GET

```diff
+ http://127.0.0.1:8000/product/list/
```
> response
```json
[
    {
        "id": 4,
        "name": "orange",
        "price": 0.0,
        "seller": 1
    },
    {
        "id": 3,
        "name": "Cameron Bass",
        "price": 474.0,
        "seller": 1
    },
    {
        "id": 2,
        "name": "Ignatius Alston",
        "price": 978.0,
        "seller": 2
    }
]
```

### add product POST

```diff
! http://127.0.0.1:8000/product/list/
```
> body
```json
{
    "name":"oranges",
    "seller": 2,
    "price":500
}
```

> response
```json
{
    "id": 6,
    "name": "oranges",
    "price": 500.0,
    "seller": 2
}
```

### get product by seller GET

```diff
+ http://127.0.0.1:8000/product/list/?search=admin
```
> response
```json
[
    {
        "id": 4,
        "name": "orange",
        "price": 0.0,
        "seller": 1
    },
    {
        "id": 3,
        "name": "Cameron Bass",
        "price": 474.0,
        "seller": 1
    },
    {
        "id": 5,
        "name": "oranges",
        "price": 500.0,
        "seller": 1
    },
    {
        "id": 1,
        "name": "Shea Ochoa",
        "price": 686.0,
        "seller": 1
    }
]
```
### get your product GET

```diff
+ http://127.0.0.1:8000/user/my-product/
- headers { 'Authorization' : 'Token eb7c0e9789f2166697bcc6b43ab8deb447acddf3 '}

```
> response
```json
[
    {
        "id": 4,
        "name": "orange",
        "price": 0.0,
        "seller": 1
    },
    {
        "id": 3,
        "name": "Cameron Bass",
        "price": 474.0,
        "seller": 1
    },
    {
        "id": 5,
        "name": "oranges",
        "price": 500.0,
        "seller": 1
    },
    {
        "id": 1,
        "name": "Shea Ochoa",
        "price": 686.0,
        "seller": 1
    }
]
```


