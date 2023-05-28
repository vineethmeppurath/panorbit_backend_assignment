# panorbit_backend_assignment

# Django Project

This Django project provides user creation.

## Requirements

- Python 3.6 or higher
- Django 3.2 or higher

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/your-username/your-project.git

2. Navigate to the project directory:

cd your-project/

3. Create and activate a virtual environment:
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

4. Install the project dependencies:

pip install -r requirements.txt

## Database Setup

1. Create a database (or use any other database of your choice) and update the database settings in `settings.py`.

2. Run the database migrations:

python manage.py migrate


## Running the Development Server

Start the Django development server with the following command:

python manage.py runserver

Access the project in your web browser at `http://localhost:8000/`.


## Swagger Documentation

The project is integrated with Swagger to provide API documentation.

1. Access the Swagger UI in your web browser at `http://localhost:8000/api/swagger/`.

2. Explore the available API endpoints, request/response parameters, and test the API directly from the Swagger UI.

## Usage

1. Open the signup API endpoint.
2. Click on the "Try it out" button.
3. Input the following details:
      First Name: [your first name]
      Last Name: [your last name]
      Email: [your email address]
      Gender: [your gender]
      Phone Number: [your phone number]
4. Once you have entered the required information, click the "Execute" button.
By following these steps, you can successfully sign up by providing your first name, last name, email, gender, and phone number as input.
