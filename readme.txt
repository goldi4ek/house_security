# House Security Application

## Overview
This is a Django-based web application for managing house security. It includes features for user authentication, house management, and more.

## Prerequisites
- Python 3.x
- Django 3.x or later
- SQLite (default database)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/goldi4ek/house_security
    cd house_security
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Apply the migrations to set up the database:
    ```sh
    python manage.py migrate
    ```

## Running the Application

1. Start the development server:
    ```sh
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test