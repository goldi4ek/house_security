# House Security Application

## Installation

1. Install pipenv if you haven't already:

   ```sh
   pip install pipenv
   ```

2. Install the required dependencies using pipenv:

   ```sh
   pipenv install
   ```

3. Activate the virtual environment:

   ```sh
   pipenv shell
   ```

4. Apply the migrations to set up the database:

   ```sh
   python manage.py migrate
   ```

5. Create a superuser for accessing the admin interface:
   ```sh
   python manage.py createsuperuser
   ```

## Running the Application

1. Start the development server:

   ```sh
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.
