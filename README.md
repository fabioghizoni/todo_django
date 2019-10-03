# todo_django

To start the server:

```sh
$ docker-compose up
$ docker exec -it app_todo python manage.py makemigrations
$ docker exec -it app_todo python manage.py migrate
```

Creating django superuser (feel free to change name and email):

```sh
$ docker exec -it app_todo python manage.py createsuperuser --email admin@example.com --username admin
```

For accessing the postgres container shell if needed:
```sh
docker exec -it db_todo psql -U postgres postgres
```



## For now it does:

- Creates a new User (endpoint: /api/users POST);
- Lists all users for admins (endpoint: /api/users GET);
- Retrieve a user for admins or the user (enpoint: /api/users/|user_pk| GET);
- Delete a user for admins or the user (enpoint: /api/users/|user_pk| DELETE);
- Authentication and login (endpoint: /api/auth/login POST);
- Sends email for password retrieving using Sendgrid (endpoint: /api/psw_retrieve POST);
- New password is created, saved and sent to the email if valid (still not checking if email is real).


## Problems:
- There are nesting url problems as far as /api/users/|user_pk|/todos POST is not creating new entries correctly;
- The API is not creating new todo_lists, let alone new tasks;
- Env variables such as SECRET_KEY and the SendGrid API Key are not hidden from the settings.py file;
- Still in development environment, it is using docker-compose, so the image needs to be built first.

