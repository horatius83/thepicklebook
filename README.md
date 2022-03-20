# thepicklebook

I wanted to re-learn Django (and Vue.js) so I figured I'd design a pickle-based social network

The pickle data is partially seeded from [The Open Grocery Database Project](https://www.grocery.com/open-grocery-database-project/)

## Setting up your environment

You'll need the following environment variables set:

- **DJANGO_POSTGRES_DB_NAME** the name of the database
- **DJANGO_POSTGRES_USER_NAME** the user name for the database
- **DJANGO_POSTGRES_PASSWORD** the password for the database
- **DJANGO_POSTGRES_HOST** the host of the database
- **DJANGO_POSTGRES_PORT** the port of the database
- **DJANGO_SECRET** the secret key to use for the application

If you're doing local development with a dockerized postgres instance, you'll also need to set up a **.env** file in the ./db directory:

```
POSTGRES_USER: <user>
POSTGRES_PASSWORD: <password>
POSTGRES_DB: <database name>
```

Make sure these values equal the values in the environment values. Also if you are planning to use a post other than **5432** update the **docker-compose.yml** file. For instance, if your new port is 7777 then the ports section would read **7777:5432**

## Running Locally

Once you've set up your system environment variables, open a terminal window, navigate to ./db and enter the command `docker compose up`. In a second terminal window, navigate to the base directory and run `python manage.py runserver`