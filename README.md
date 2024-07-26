# Team Member Management Application

This application is designed to manage team members efficiently, allowing users to view, add, edit, and delete team members. The application is built with Django and can be set up to run locally with minimal setup.

## Features

- **List Team Members:** View all team members with an indication if a member is an admin.
- **Add Team Members:** Add new team members by specifying their name, phone number, email, and role.
- **Edit Team Members:** Update details of existing team members or change their roles.
- **Delete Team Members:** Remove team members from the system.

## Installation

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Homebrew (for macOS users)
- Python 3.8 or higher
- pip
- Virtualenv (optional but recommended)

### Setup on macOS

If you are using macOS and do not have Python installed, you can install it using Homebrew:

```bash
brew install python

### Set Up Virtual Environment

# Install virtualenv if it is not installed
pip install virtualenv

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

### Install Dependencies

# Install Django and the PostgreSQL adapter for Python
pip install django
pip install psycopg2-binary

### Initialize the Database

# Make migrations to create database schema
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run the Server
python manage.py runserver
