# assignment-2 Solution

I opted for using JWT tokens. The private key is stored on an environment variable set on docker-compose.yml.

JWT is a good option because it's an already existing standard and don't require storing and expiring the tokens in a database.

Ideally private keys and passwords would not be commited to git. A 'vault' or 'secret' should be used instead.

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


