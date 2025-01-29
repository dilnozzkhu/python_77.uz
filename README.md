# python_77.uz - Backend System for Buying and Selling Products


# Introduction
python_77.uz is a backend system designed to power an online platform for buying and selling products. The system offers secure, well-documented, and user-friendly APIs, compliant with Swagger standards, ensuring smooth integration and interaction. It also features a clean Django admin interface for efficient management of users, products, and roles. The platform is built with security and usability in mind.

# Roles

| **Role Name**   | **List of Permissions (Logical Modules)**                   | **Role Description**                                             |
|-----------------|-------------------------------------------------------------|------------------------------------------------------------------|
| Super Admin     | All permissions                                             | Project manager overseeing the entire system.                    |
| Admin           | Adding sellers, generating login and password               | Manages new seller accounts.                                     |
| Seller          | Adding/removing products                                    | Cannot access the admin panel.                                   |

# Project Languages
Uzbek (Latin alphabet)
Russian
# Technologies Used:
Django: Python-based web framework for rapid development.
Django Rest Framework (DRF): Toolkit for building Web APIs.
PostgreSQL: Database for storing user data, products, and transactions.
JWT Authentication: JSON Web Tokens for secure API access.
drf-yasg: For auto-generating Swagger documentation.
# Installation
Prerequisites
Ensure you have the following installed:

Python
Django Rest Framework (DRF)
Installation Steps
# Clone the repository
git clone https://github.com/dilnozzkhu/python_77.uz.git

# Navigate to the project directory
cd python_77.uz

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver


Log in as an admin to manage users and products.

Use the Django admin panel to manage platform content:
http://127.0.0.1:8000/admin/

Test APIs using Swagger:
Navigate to the API documentation endpoint (if available in the project).

Use tools like Postman or curl for manual API testing.
