## 🏠 Property Listings API with Caching

This is a Django-based API for managing and retrieving property listings. The project is designed to be highly performant by leveraging Redis as a caching layer. The entire application is containerized using Docker and Docker Compose for easy setup and consistent environments.

### 📝 Features

- **RESTful API**: An API endpoint to list all available properties in JSON format.
- **View-Level Caching**: The API response is cached in Redis to reduce server load and improve response times for frequent requests.
- **Low-Level Queryset Caching**: The database query for all properties is cached at a low level, allowing other parts of the application to also benefit from the cached data.
- **Cache Invalidation**: The cache is automatically invalidated whenever a property is created, updated, or deleted, ensuring that users always see fresh, up-to-date data.
- **Cache Metrics**: The application provides metrics (hits, misses, and hit ratio) to help analyze the effectiveness of the caching strategy.
- **Containerized Development**: The entire application, including the Django app, PostgreSQL database, and Redis cache, runs in a multi-container Docker environment.

### 🚀 Getting Started

These instructions will get a copy of the project up and running on your local machine.

#### Prerequisites

- Docker and Docker Compose installed on your system.

#### Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FrankieWilson1/alx-backend-caching_property_listings.git
   cd alx-backend-caching_property_listings
   ```

2. Build and run the Docker containers:
   This command will build the Django app container, start all three services (web, db, and redis), and run them in the background. It also includes a health check script to ensure the database is ready before the Django app starts.
   ```bash
   docker-compose up --build -d
   ```

3. Run database migrations:
   Even with the automatic migration command in `docker-compose.yml`, it's good practice to run it manually after the initial setup to ensure everything is in sync.
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:
   To access the Django admin panel and add properties, you'll need to create a superuser.
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### 🧪 Usage

Once the containers are running, you can interact with the API:

- **View Property Listings**: Navigate to this URL in your browser or use a tool like curl or Postman.
  ```
  http://localhost:8000/api/v1/properties/
  ```

- **Add/Update/Delete Properties**: Log in to the Django admin panel to manage properties. Changes made here will automatically invalidate the cache.
  ```
  http://localhost:8000/admin/
  ```

- **Monitor Cache Metrics**: Every time you access the properties API endpoint, the Redis cache metrics will be logged to your terminal. To view these logs, use:
  ```bash
  docker-compose logs -f web
  ```
  You will see output indicating cache hits, misses, and the current hit ratio.
