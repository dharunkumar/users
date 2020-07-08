This Django application provides 
1.populate.py management command to populate database with random data of users
    a.This command can be run by "python manage.py populate --users 10 --activities 4"
    b.--users option specifies no.of users to be created
    c.--activities option specified no.of activities to be created per user
2.API endpoint to get user's data and their activity periods, this endpoint only supports "GET" request method.