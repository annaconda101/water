# Water 
(A simple question and answer app using Django forms)

# Description:
This is a coding exercise built in Django that contains a form to add a question.
Once a question is added, users can post answers on the page and are able to upvote or downvote.
The answers are ordered in descending order, having the answer with the most votes at the top.


# Prerequisites
## homebrew
1. [installation](http://brew.sh/)

## postgres
1. `brew install postgres`
2. `postgres -D /usr/local/var/postgres`


# Installation
1. `virtualenv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`


# Usage
1. `python manage.py runserver`
2. navigate to `http://127.0.0.1:8000/`

# Testing
1. `python manage.py test fire`
