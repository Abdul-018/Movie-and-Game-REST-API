
# Movies & Games Vault API

A simple REST API built with **FastAPI** for storing and managing movies and games.

## Features

* List all media items.
* Filter items by type (`movie` or `game`).
* Retrieve an item by ID.
* Create a new media item.
* Update an existing media item.
* Delete an item.
* Validate request data with Pydantic.

## Data Model

Each media item contains:

| Field          | Type             | Required      | Description                     |
| -------------- | ---------------- | ------------- | ------------------------------- |
| `id`           | integer          | Response only | Unique item ID                  |
| `title`        | string           | Yes           | Movie or game title             |
| `type`         | `movie` | `game` | Yes           | Media type                      |
| `release_year` | integer          | Yes           | Release year, from 1888 to 2030 |
| `genre`        | string           | Yes           | Genre of the item               |
| `rating`       | float            | No            | Rating from 0.0 to 10.0         |

The API starts with two example records: **Kabhi Khushi Kabhi Gham** and **Fortnite**.

## Requirements

Install the required Python packages:

```bash
pip install fastapi uvicorn pydantic
```

## Running the API

Save the application as `main.py`, then run:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI also provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Get all items

```http
GET /items
```

Returns all movies and games.

### Filter by type

```http
GET /items?item_type=movie
```

or:

```http
GET /items?item_type=game
```

The `item_type` filter accepts `movie` or `game`.

### Get an item by ID

```http
GET /items/{item_id}
```

Example:

```http
GET /items/1
```

Returns a 404 error if the requested item does not exist.

### Create an item

```http
POST /items
```

Example request body:

```json
{
  "title": "The Legend of Zelda",
  "type": "game",
  "release_year": 1986,
  "genre": "Adventure",
  "rating": 9.0
}
```

The API automatically generates the next available ID.

### Update an item

```http
PUT /item/{item_id}
```

Example:

```http
PUT /item/1
```

with a JSON body containing the updated media information.

### Delete an item

```http
DELETE /item/{item_id}
```

Example:

```http
DELETE /item/2
```

The API returns a message containing the title of the deleted item.

## Storage

The application currently uses an in-memory Python list as its database.

This means data is lost whenever the application restarts.

## Project Structure

```text
.
├── main.py
└── README.md
```

## Notes

The current implementation is a small example API and does not use a persistent database. It is suitable for learning and experimentation with FastAPI, Pydantic models, CRUD operations, path parameters, and query parameters.
