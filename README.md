# Python task

Python task is a Django-based e-commerce platform that allows users to create shops, add products, manage orders, and more.

## Installation

Clone the repository:
```
$  bash
   git clone https://github.com/turgunovjasur/Python-task
```
Create a virtual environment and activate it:
```
$  python3 -m venv env
source env/bin/activate
```
Install the dependencies:
```
$  pip install -r requirements.txt
```
Run migrations:
```
$  python manage.py migrate
```
Create a superuser:
```
$  python manage.py createsuperuser
```
Run the development server:
```
$  python manage.py runserver
```


## Usage

```
$ Access the admin panel at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
```
```
$ Create shops, add products, manage orders, and view analytics.
```

## Features

* Custom user model and user profile.
* Product inventory management.
* Category hierarchy for products.
* Image upload for products and shops.
* Order management with different order statuses.
* Integration with payment systems for online transactions.
* Search functionality for products.
* Pagination for product lists.
* SMS-based user registration.
* Discount announcement system based on user interactions.
* Analytics dashboard for sales and user activities.

## Technologies Used

* Python Django
* Django REST Framework
* PostgreSQL
* Pillow
* Psycopg2
* Django admin soft dashboard
* Vue.js

## Contributors

* Jasur

## License

* MIT License

