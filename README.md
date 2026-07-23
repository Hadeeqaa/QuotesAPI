
# Quotes API 
A REST API for authenticated quote lister, users register and log in via JWT then hit an endpoint to get a random quote (or a list of quotes). Built with Django REST Framework using a service-layer architecture to keep business logic separate from views.

## Features 
- get a quote or list of quotes randomly
- only logged in users get result based on the endpoint
- quotes database is expanded through a superuser Admin
- allows user to reroll the result by hitting endpoint again
  
## Tech Stack
- language: python
- framework: django rest framework
- usage : Postman,terminal, Hoppscotch, 

## Setup
```
git clone https://github.com/Hadeeqaa/QuotesAPI.git
cd QuotesAPI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Create a .env file in the project root with your own values:
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
SECRET_KEY=your-django-secret-key
DEBUG=True

Generate a secret key with: python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```
- Run migrations and start the server:

```
python3 manage.py migrate
python3 manage.py createsuperuser   # to add quotes via Django Admin
python3 manage.py runserver
```
Usage

1. Register a new user

```
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "yourname", "password": "yourpassword"}'
```
2. Log in to get a JWT token

```
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "yourname", "password": "yourpassword"}'

This returns an access token.
```
3. Request a quote using the token
```
curl -H "Authorization: Bearer <your_access_token>" \
  http://127.0.0.1:8000/api/quote/
```

## Further Improvements
- Expand quotes database to 300+ entries
- Add pagination for multi-quote requests
- Deploy to AWS (Elastic Beanstalk + RDS)
