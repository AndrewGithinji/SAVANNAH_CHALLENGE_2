# SAVANNAH_CHALLENGE_2

The project is a contemporary web development initiative, incorporating cutting-edge practices such as containerization, orchestration, and a robust emphasis on testing, security, and CI/CD processes. It aligns closely with industry-standard tools and frameworks, demanding a comprehensive understanding of the complete software development lifecycle.

## Getting Started

These instructions will help you set up and run the project on your local machine for development purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.11)
- PostgreSQL
- Pipenv (optional but recommended)

### Installation

1. **Clone the repository:**

   bash
   git clone https://github.com/AndrewGithinji/SAVANNAH_CHALLENGE_2.git

2. **Create a virtual environment (optional but recommended):**

    python3 -m venv venv
    source venv/bin/activate  # Activate the virtual environment

3. **Apply Migrations:**

    python manage.py makemigrations
    python manage.py migrate

4. **Create Superuser (if using Django Admin):**

    python manage.py createsuperuser

5. **Run the development server:**

    python manage.py runserver
    The application should now be running at http://localhost:8000.

6. ### Running Tests

# To run tests and check coverage:

coverage run --source='.' manage.py test
coverage report

## Deployment

* Instructions on how to deploy this project to a live system will be added later.

## Built With

* Django - The web framework used

* PostgreSQL - Database system

* Django OAuth Toolkit - OAuth2 provider for Django

* Social Auth App Django - Social authentication for Django



