# IP-to-AWS-region-API

Api that creates users with emails, passwords and their AWS region. AWS region gets autofilled if not specified.

To run the app:
```
docker-compose up
```

The user management dashboard will be accessible from either:
```
127.0.0.1:8080/api/user/create/
```

or
```
<ip_of_docker_compose_machine>:8080/api/user/create/
```

# Using the API
In the remainder of this readme, it is assumed that a Debian-based machine is being used.

After the container is launched, then, to create a new user, use a curl command like the one below:

```
curl -X POST -H "Content-Type: application/json" \
-d '{ "email": "testuser@gmail.com", "password": "passwordstrong0000", "name": "Test Person"}' \
http://<ip_of_docker_compose_machine>:8080/api/user/create/
```

# Using the tests

This API was implemented using TDD. To run all the tests, run the following command:

```
docker-compose run app sh -c "python manage.py test"
```
