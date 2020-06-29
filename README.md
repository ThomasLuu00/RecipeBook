# RecipeBook
A web-based recipe editor and viewer.

## Features for 1.0.0
- Store recipes online.
- Browse and edit recipes.

## Setup
All the instructions aree relative to the project root.

### Requirements
- Python >= 3.6
- Angular
- Docker
- Docker-Compose

### Run dev stack
```bash
docker-compose build
docker-compose up

# New shell
docker pm   # Copy the id for the dj container
docker exec -it <dj-id> python manage.py migrate
```

### Run dev for angular 
```bash
cd angular/angular-app
ng serve
```
## References
- https://dragonprogrammer.com/dockerized-django-api-angular-tutorial/
