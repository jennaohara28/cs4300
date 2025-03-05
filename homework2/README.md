http://76.155.212.102:4300/movie-list/

This is a simple Django application for managing movie theater bookings. It allows users to view available movies, book seats, and view their booking history.

## Features
- List of available movies
- Seat booking functionality
- Booking history for users

---

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Django
- Django REST Framework

---

### Steps to Set Up the Project

1. **Clone the repository**:
   If you haven't already, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/jennaohara28/cs4300
   cd homework2

2. Set up a virtual environment (optional but recommended): Create a virtual environment to manage dependencies:
python3 -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3. Install dependencies: Install the required packages using pip:

pip install django djangorestframework

4. Apply migrations: Run the migrations to set up your database:

python manage.py migrate

5. Create a superuser (optional but recommended for admin access):

python manage.py createsuperuser
Follow the prompts to create the superuser.

6. Start the development server: To start the Django development server, run:

python manage.py runserver 0.0.0.0:4300

This will start the server on port 4300. You should now be able to access the site by navigating to http://localhost:4300 in your web browser.

7. Access the Admin Panel: You can access the Django admin panel at:

http://localhost:4300/admin/
Log in with the superuser credentials you created earlier.

API Endpoints
If you're working with the API, here are the available endpoints:

GET /api/movies/ - Retrieve all movies
GET /api/seats/ - Retrieve all available seats
GET /api/bookings/ - Retrieve all bookings
vbnet

## Acknowledgements

I would like to acknowledge the use of ChatGPT by OpenAI for assistance with project-related tasks, including code examples, explanations, and debugging help.

