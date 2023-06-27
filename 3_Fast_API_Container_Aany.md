# FastAPI and Docker

Now that we created the api that connects to the Database, we can create a Docker image for the api and run it in a container. We will use the Dockerfile that we created in the previous section to create the Docker image. We will also use the docker-compose.yml file to run the api in a container.

For that please create a Dockerfile in the service folder with the following content:

```Dockerfile
# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Building the Docker Image
To build the Docker image, we need to run the following command inside the service folder:

```bash
docker build -t fastapi .
```

### Building your (Virtual) Network

```bash
docker inspect <container_id> | grep IPAddress

docker inspect eded01401b0c | grep IPAddress
```

To create a virtual network, we can use the `docker network create` command:

```bash
docker network create <network_name>
```
```bash
docker network create kchousedata
```

To list all the virtual networks, we can use the `docker network ls` command:

```bash
docker network ls
```

### Connecting Containers to a Network

To connect a container to a virtual network, we can use the `docker network connect` command:

```bash
docker network connect <network_name> <container_id>
```

```bash
docker network create kchousedataeded01401b0c
```

### Running the FastAPI Container
To run the Docker container, we need to run the following command:

```bash
docker run -d --name fastapi --network <network_name> -e DB_CONN='postgresql://postgres:postgres@postgres:5432/postgres' -p 8000:8000 fastapi  
```

```bash
docker run -d --name fastapi --network kchousedata -e DB_CONN='postgresql://postgres:postgres@postgres:5432/postgres' -p 8000:8000 fastapi  
```

Output
b56281be497ceae8a01183645292911e6a429614fceb22d7d2ae5802b1d90657