# Bit68
## Requirements
## 1. Python Requirements
1. clone this repo
2. cd into repo root folder
3. `pip install -r requirements.txt`

<br>

## 2. Database Requirements
1. create new database with the following credential 
```json
{
  "NAME": "Bit68",
  "HOST": "localhost",
  "USER": "postgres",
  "PASSWORD": "691999",
  "PORT": 5432
}
```

<br>

## 3. Migration Requirements
1. start postgres service by run this `service postgres start`
2. cd into repo root folder
3. active you venv (if you have)
4. run this commands 
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

<hr/>

# Endpoints

## 1. Seller

### 1.1 get all users GET

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

### 1.2 register POST

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


### 1.3 login POST

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
<hr/>

## 2. Product

### 2.1 get all products GET

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

### 2.2 add product POST

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

### 2.3 get product by seller GET

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
### 2.4 get your product GET

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


