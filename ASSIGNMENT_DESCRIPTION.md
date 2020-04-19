# assignment-2

This task aims to touch **backend**, **containers** and **Kafka**. At Fuelsave the three go side-by-side to speed up deployment and are a central part of our software development pipeline.

This repository has an api boilerplate that uses [fastapi](https://fastapi.tiangolo.com/) and `nginx`. Feel free to complement as you please. 


### Tips 
* running the `app/main.py` script will launch the api at `localhost:8080`
* most likely you need to sign-in Docker to make the docker-compose run out of the box.

### Data
There are 2 files inside the data folder, in csv, to support the assignment:
* users: username|password 
* vehicles: id|distance|owner

# To be evaluated:
Each vehicle has an owner (user). A user can only see information regarding their vehicles.   

* Build 2 endpoints:
  * One for authentication with route `POST /token`. Given a valid username-password, return a token with an encryption of your choice. The token should expire in 10 minutes
  * One for an authenticated user to fetch information on all its vehicles, sort by distance, with route `GET /vehicles`. Given an encrypted username, decrypt and return the vehicles
* Add the data to a database of your choice and integrate in the docker-compose.
* Implement unit tests.
* Integrate Kafka in the docker-compose, it should produce messages to a specific `fuelsave`.

### Bonus
* Build an endpoint with route `GET /messages` that returns the last 10 messages from the `fuelsave` Kafka topic. 

### Deliverables:

* The task is estimated to take 8h.
* Your API is expected to be running at `localhost:80` with the command `docker-compose up`.

### How to submit?
Send us a link to a source control repository. Make sure your solution includes a README.md, documenting assumptions, simplifications and/or choices you made, as well as a short description of how to run the code and/or tests. 
Finally, to help us review your code, please split your commit history (at least separate the provided code from your solution).

### Next steps:
After you submit your code, we will contact you with feedback and potentially arrange a face2face interview with the team. 
The interview will be not only about reviewing the challenge but also discussing topics such as company culture, engineering, management and others.




