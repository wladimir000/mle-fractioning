# Bonus Solution

This folder contains a small, working reference implementation for the optional stretch goal from the project brief. It stays close to the patterns used in the API lecture so it is easier to compare with what you have already seen. It is meant to be a runnable example, not the only correct way to solve the bonus task.

## What It Includes

- A minimal FastAPI CRUD API
- A Postgres database
- A `Dockerfile` for the API
- A `docker-compose.yaml` file that starts both services together

## House Resource

The example `House` resource stores the following five fields:

- `bedrooms`
- `bathrooms`
- `sqft_living`
- `grade`
- `zipcode`

## API Endpoints

- `POST /houses`
- `GET /houses`
- `GET /houses/{house_id}`
- `PUT /houses/{house_id}`
- `DELETE /houses/{house_id}`

## Run the Stack

1. Copy `.env.example` to `.env` if you want to customize the defaults.
2. From this folder, run:

```bash
docker compose up --build
```
3. Open <http://localhost:8000/docs> to explore the API.

## Local Example Request

```bash
curl -X POST http://localhost:8000/houses \
  -H "Content-Type: application/json" \
  -d '{
    "bedrooms": 3,
    "bathrooms": 2.5,
    "sqft_living": 1800,
    "grade": 8,
    "zipcode": "98103"
  }'
```

## Notes

- Tables are created automatically when the API starts.
- The database is persisted in the `postgres_data` Docker volume.
- This example is intentionally small so it is easy to study and adapt.
