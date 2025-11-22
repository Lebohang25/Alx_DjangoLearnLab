# advanced_features_and_security

Django project scaffold for the "Advanced Features and Security" assignment.

Quick start:

1. Create virtualenv and install requirements
   - python -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt

2. Create `.env` file (optional) with SECRET_KEY and DEBUG

3. Run migrations:
   - python manage.py makemigrations
   - python manage.py migrate

4. Create superuser:
   - python manage.py createsuperuser

5. Serve locally (development):
   - python manage.py runserver

Note: for media upload, ensure MEDIA_ROOT exists.
