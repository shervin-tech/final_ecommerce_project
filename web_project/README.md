# Django E-commerce Website

A modern e-commerce website built with Django, featuring product management, shopping cart, and secure checkout.

## Features

- User authentication and registration
- Product catalog with categories
- Shopping cart functionality
- Secure checkout with Stripe integration
- Admin dashboard for product management
- Responsive design

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the website at http://127.0.0.1:8000/

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
``` 