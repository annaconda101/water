# Water 
(A simple question and answer app using Django forms)

# Description:

This is a work in progress app and we will be aiming to change this to a pet owner's portal.
This is built in Django that contains a form to add a question.
Once a question is added, users can post answers on the page and are able to upvote or downvote.  Once the answers are added, they will be rendered with a sentiment score.
The answers are ordered in descending order, having the answer with the most votes at the top.

This also features a section called 'doggly' where users can add random facts about dogs.  Once the fact is added on the page, a random photo of the dog will be displayed (done via the https://dog.ceo/dog-api/).


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
4. `python -m textblob.download_corpora` (This is necessary as it is used for sentiment analysis of the answers)
5. `python manage.py migrate`


# Usage
1. `python manage.py runserver`
2. navigate to `http://127.0.0.1:8000/` for Question and Answers app 
3. navigate to `http://127.0.0.1:8000/doggly` for Doggly (Facts displayer with photo)

# Testing
1. `python manage.py test fire`
