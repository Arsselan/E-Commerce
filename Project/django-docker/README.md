[comment]: <> (author: Sarish)   
# Django App with PostgreSQL in Docker

This guide will help you to start the django and postgres containers.
## Prerequisites

- Docker: Ensure that Docker is installed on your system.

**Definition Dockerfile**
   - The Dockerfile defines how the container will be built and what dependencies need to be installed.

**Definition docker-compose.yml:**
   - This file defines services such as the PostgreSQL database and the Django application.

## Steps
1. **Build and Start Docker Containers:**
   - Run `docker-compose up --build` to create and start the containers. The `--build` option is necessary if the Dockerfile changes. Use docker-compose up -d --build in order to run it in the background.

2. **Run Django Commands in the Container:**
   - Execute Django commands in the container, e.g., create migrations or restart the development server by using `docker-compose run web python manage.py migrate` or `docker-compose restart web db`.

3. **Stop Docker Containers:**
   - Stop the Docker containers with `docker-compose down` when development is complete.
