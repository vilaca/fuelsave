# assignment-2 Solution

I opted for using JWT tokens. JWT is a good option because it's an already existing standard and doesn't require storing and expiring the tokens in a database.

The private key used for generating the jwt tokens is stored in an environment variable set on docker-compose.yml. Ideally private keys and passwords would not be committed to git. A 'vault' or 'secret' should be used instead.

For importing users.csv and vehicles.csv my first option was a script that would run on the first the db container but the script became a bit too long and was doing the work of creating the tables that can be also done using the pydantic models. In the end I implemented loading the csv files in python when the app server starts.

Passwords from users.csv are now hashed and salted before being stored on the users table. The Hash is set in docker-compose as an environment variable.

The owner fields in vehicles.csv is a string and not very efficient. A possible future improvement is to use a foreign key with the primary key from table users.

For the purpose of having a rest service /messages to retrieve last n messages received a more scalable solution would be to have a small process listenning on the kafka topic and storing the last N messages. The rest service would only pool the process storage and get its contents.

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

To login with 'user1' and get an API-KEY:
```shell
curl -X POST "http://localhost/token" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"username\":\"user1\",\"password\":\"pass1\"}"
```

To list vehicles for user w/ API-KEY in header:
```shell
curl -H 'Accept: application/json' -H "Authorization: Bearer <API-KEY>" http://localhost/vehicles
```

To list vehicles for user w/ API-KEY as a query string parameter:
```shell
curl -H 'Accept: application/json' "http://localhost/vehicles?api-key=<API-KEY>"
```


To generate private key for JWT and salt for password hashing:
```shell
openssl rand -hex 32
```

To queue some messages into the fuelsave topic:
```shell
docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic fuelsave
```

