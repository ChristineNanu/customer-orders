# Customer Orders

Manage customers and orders via a REST API.

## Requirements

- Ensure you've installed [Docker](https://docs.docker.com/get-docker/).

## Getting Started

- Clone the repository and navigate to its top-level directory.
- Copy the file `.env.example` to `.env`:
  ```
  cp .env.example .env
  ```
- Build and start the container:
  ```
  
  docker compose up --build
  ```
- Subsequent runs of the machine require only:
  ```
  docker compose up
  ```

The app is accessible at http://localhost:8000/. The API docs are hosted at http://localhost:8000/api/.

## Useful Commands

- To run migrations:
  ``` 
  docker exec -i customer_orders_web python manage.py makemigrations
  ```
- To apply migrations:

  ```
  docker exec -i customer_orders_web python manage.py migrate
  ```

- To run tests:

  ```
  docker exec customer_orders_web python manage.py test
  ```

- To run coverage:

  ```
  docker exec customer_orders_web coverage run manage.py test
  ```

- To generate a coverage report:

  ```
  docker exec customer_orders_web coverage report -m
  ```

- To open the db shell:
  ```
  docker exec -it customer_orders_db psql -U user -d customer_orders
  ```
