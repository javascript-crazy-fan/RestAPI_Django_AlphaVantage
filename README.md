# RestAPI_Django

## Setup

- Clone RestAPI_Django project.
- Turn on Docker on your local machine.
- Run command:
    ```
    $ docker-compose build
    ```

    ```
    $ docker-compose up
    ```

- Create SuperUser
    ```
    $ docker exec -it <container_id> python manage.py createsuperuser
    ```

- Generate New API Key
    ```
    $ Login to admin panel (<server url>/admin)and create API Key
    ```

## Testing

- Run command:
```
$ docker-compose run --rm app sh -c "python manage.py test && flake8"
```

## API endpoints

- `GET /api/v1/quotes`
- `POST /api/v1/quotes`