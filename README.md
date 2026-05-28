> just having a  look at what DRF has to provide. Seems like every solution is just one import away. 
# Blog API

A Blog API built with Django 6.0 and Django REST Framework following the book Django for Api by William S. Vincent.

## Features

- **Authentication**: Secure Token and Session-based security via `dj-rest-auth`.
- **User Management**: Custom user model supporting registration, profile updates, and admin-level controls.
- **Permissions**: Custom granular control (Authors can edit their own posts; Admin-only user management).
- **API Documentation**: Automated OpenAPI 3.0 schema generation with interactive Swagger UI and ReDoc.
- **Configuration**: Secure, environment-based settings using `environs`.

## Quick Start

1. **Environment Setup**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

2. **Installation**
   ```bash
   # Install dependencies using uv
   uv pip install django djangorestframework django-cors-headers dj-rest-auth django-allauth drf-spectacular "environs[django]"

   # Run migrations
   uv run python manage.py migrate
   ```

3. **Run the Server**
   ```bash
   uv run python manage.py runserver
   ```

## API Reference

Explore the endpoints using the built-in documentation:
- **Swagger UI**: http://127.0.0.1:8000/api/schema/swagger/
- **ReDoc**: http://127.0.0.1:8000/api/schema/redoc/

### Key Endpoints
- `/auth/` — Login, logout, and password management.
- `/auth/signup/` — New user registration.
- `/users/` — User management (Admin/Owner restricted).
- `/api/v1/` — Blog post operations.

## Tech Stack
- **Package Manager**: uv
- **Backend**: Django 6.0, Django REST Framework
- **Authentication**: dj-rest-auth, django-allauth
- **Documentation**: drf-spectacular (OpenAPI 3.0)
