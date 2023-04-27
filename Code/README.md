# Presentation

This code scrap data from Twitter and add them to a MongoDB database.
It also attribute a reliability score to the scrapped accounts reprensenting their likelyhood of spreading false informations.
The higher the score the less likely that this account is spreading false information.

CAREFUL !! 
This is a check with limited parameters it should not be taken for granted that a high relibility score mean truthful news.
Please alway double check your sources

## How to use :

You must run main.py with three arguments (not caps sensitive):
1. action :
    * "scrap" : scrap users data and add them to the database updating if not already existing
    * "getusers" : print users information in the console
    * "getreliability" : print the users reliability score
2. network :
    * "twitter" : scrap on twitter
3. users : list all the usernames separated by comas (do not use spaces)

example :

.\main.py scrap twitter elonmusk,nytimes

## Database

By default this database is local, you can change this by altering the constant DATABASEADRESS in DataLink.py.

