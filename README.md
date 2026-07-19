
# Quotes API 
a quotes randomizer that shows a number of quotes randomly based on the number selected only to logged in users.

## Features 
- get a quote or list of quotes randomly
- only logged in users get result based on the endpoint
- quotes database is expanded through a superuser Admin
- allows user to reroll the result by hitting endpoint again
- 
## Tech Stack
- language: python
- framework: django rest framework
- usage : Postman, Hoppscotch


## Usage 
```bash
git clone https://github.com/Hadiqaaaa/pricecompare
cd userapi
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

create a `.env` file
```
DB_NAME=quotesapi
DB_USER=quotesuser
DB_PASSWORD=changeme123
SECRET_KEY='django-insecure-(_=qs=l!d*x+!hskxquis0#9-bqv4_vddx)72q9w%2z+9w$#1@'
DEBUG=True
```
then run
```
python3 manage.py runserver
```
for instance : test endpoint through cli terminal 
```
curl -H "Authorization (Bearer Jwt Token)" "url endpoint"
```
## further imrpovements
- expanding database to 300 quotes without lag 
- allowing users to reroll 
- letting users select from a range of quotes 

