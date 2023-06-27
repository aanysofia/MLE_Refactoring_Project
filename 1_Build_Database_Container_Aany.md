## Building a Docker Image


```Dockerfile
# Use the official PostgreSQL image as the base image
FROM postgres:13.2

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 5432

# Run the application
CMD ["postgres"]    
``` 

## Building the Docker Image

To build the Docker image, we need to run the following command:

```bash
docker build -t postgres .
```

## Running the Database Container
A Docker container is defined as a running instance of a Docker image. To run the database container, we need to run the following command:

```bash
docker run -d --name postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_DB=fastapi \
    -v $(pwd)/postgres-db-volumne:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

## Connecting to the Database
To connect to the database, we need to use a database client. We can use the `psql` command-line tool to connect to the database. To connect to the database, we need to run the following command:

```bash
psql -h localhost -p 5432 -U postgres
```

## Creating the Database

We already defined a database named `fastapi` in the env variables in the dockerfile. But we can also create the database using the following command:

```sql
CREATE DATABASE KCfastapi;

## Creating the Table
To create the table, we need to run the following command:

CREATE TABLE kingcountydata (
    id SERIAL PRIMARY KEY,                                                                                   
    price DECIMAL NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms DECIMAL NOT NULL,
    sqft_living INTEGER NOT NULL
);

## Inserting Data
To insert data into the table, we need to run the following command:

```sql
INSERT INTO kingcountydata (price, bedrooms, bathrooms, sqft_living) VALUES (230000, 3, 1, 75);
```


This command will insert a new row into the table


## Querying Data
To query data from the table, we need to run the following command:

```sql
SELECT * FROM users;
```

## Stopping the container

To stop the container, we can use the `docker stop` command:

```bash
docker stop <container_id>
docker stop eded01401b0c

```

