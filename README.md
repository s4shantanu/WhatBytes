# WhatBytes

# Healthcare Backend API

This is a Django REST Framework (DRF) project for managing patients, doctors, and their assignments with JWT authentication and PostgreSQL. To set up, clone the repository, install dependencies using `pip install -r requirements.txt`, configure `.env` for database and secret key, run migrations with `python manage.py migrate`, and start the server using `python manage.py runserver`. API endpoints include authentication (`/api/auth/register/`, `/api/auth/login/`), patient management (`/api/patients/`), doctor management (`/api/doctors/`), and patient-doctor mappings (`/api/mappings/`). Use Postman or `curl` for testing.
