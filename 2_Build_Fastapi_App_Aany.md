### Building a FastAPI Application

#### Creating the Database
The database was already created in 'Build_Database_Container_Aany.md' file.

#### Modular App Structure
When writing an app, it is best to create independent and modular python code in the following constituent files of our app, database.py, models.py, schemas.py, main.py.

 With a separate `database.py` and `models.py` file, we establish our database table classes and connection a single time, then call them later as needed.

To avoid confusion between the SQLAlchemy models and the Pydantic models, we will call the file `models.py` with the SQLAlchemy models, and the file `schemas.py` with the Pydantic models which are having different syntax.

#### Creating the Database Connection

The `database.py` file contains the code to create the database connection. We will use the SQLAlchemy ORM to interact with the database. SQLAlchemy is a Python library that provides a simple and powerful abstraction layer for interacting with databases. It allows us to write SQL queries using Python syntax, which makes it easy to build complex queries and perform database operations.

#### Creating the Database Models

The `models.py` file contains the code to create the database models. As before, we will use the SQLAlchemy ORM to interact with the database. 

#### Creating the Pydantic Models

The `schemas.py` file contains the code to create the Pydantic models. Pydantic is a Python library that allows us to define data models using Python type annotations. It provides data validation, serialization, and deserialization out of the box, making it easy to build robust APIs.

#### Creating the Main App File

The `main.py` file contains the code to create the FastAPI app. Here is where we bring all the modular components together.

After importing all of our dependencies and modular app components we call `models.Base.metadata.create_all(bind=engine)` to create our models in the database.

## Running the App

To run the app we can use the `uvicorn` command. The following command will run the app on port 8000:

```bash
uvicorn service.main:app --reload --port 8000
```

Now that the app is running we can access the docs in the browser at `http://localhost:8000/docs`.

## Testing the App
To test the app we can use the docs which you can access in the browser or we can use the `curl` command to send a request to the API. The following command will send a GET request to the `/kingcountydata` endpoint:

```bash
curl http://localhost:8000/kingcountydata
```
This response indicates that there is one user in the database. We can add a user by sending a POST request to the `/curl http://localhost:8000/kingcountydata` endpoint:

```bash
curl -X POST http://localhost:8000/kingcountydata -H "Content-Type: application/json" -d '{"price": 230000, "bedrooms": 3, "bathrooms": 1, "sqft_living": 75}'
``` 

```json
{
    "price": 230000, 
    "bedrooms": 3, 
    "bathrooms": 1, 
    "sqft_living": 75
}
```
his response indicates that the user was successfully added to the database. We can now send a GET request to the `/kingcountydata` endpoint to retrieve the user:

```bash
curl http://localhost:8000/kingcountydata
```

This command will return all kingcountydata.