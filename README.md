# assignment-2 Solution

I opted for using JWT tokens. JWT is a good option because it's an already existing standard and doesn't require storing and expiring the tokens in a database.

The private key used for generating the jwt tokens is stored in an environment variable set on docker-compose.yml. Ideally private keys and passwords would not be commited to git. A 'vault' or 'secret' should be used instead.

For importing users.csv and vehicles.csv my first option was a script that would run on the first the db container but the script became a bit too long and was doing the work of creating the tables that can be also done using the pydantic models. In the end I implemented loding the csv files in python when the app server starts.

GET / will redirect to /docs for the OpenApi Documentation.


To run:
```shell
docker-compose build
docker-compose up -d
```

To run unit tests:
```shell
docker-compose exec app pytest .
```


To generate secret key:
```shell
openssl rand -hex 32
```

TODO:
- encrypt passwords on table users
- kafka 
- indexes on tables


