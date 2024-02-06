# Django Gun Store Project

## Description

This is a Django project for managing a gun store. It includes models for `Gun`, `Order`, and `OrderGun`, as well as Django admin panel customization for easy order management.

## Features

- Manage guns, orders, and their quantities
- Automatic calculation of total price for orders
- Customization of Django admin panel for a user-friendly experience

## Prerequisites

- Python 3.x
- Django

## Installation

1. Clone the repository:

    
    git clone https://github.com/your-username/your-django-gun-store.git
   

2. Navigate to the project directory:

   
    cd your-django-gun-store
   

3. Create and activate a virtual environment (optional but recommended):

 
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   

4. Install dependencies:

  
    pip install -r requirements.txt


5. Apply migrations:

   
    python manage.py migrate


6. Create a superuser for Django admin access:


    python manage.py createsuperuser


7. Run the development server:


    python manage.py runserver


8. Access the Django admin panel at `http://localhost:8000/admin/` and log in with the superuser credentials.

## Usage

- Use the Django admin panel to manage guns and create orders.
- Customize the order details and quantities in the admin panel.
- Follow the paths provided in urls.py to see api views. 
