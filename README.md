# Python task
<img src=
"https://i.ibb.co/VYchgdg/1.png"
         alt="Main Page">

* Dashboard



Python task is a Django-based e-commerce platform that allows users to create shops, add products, manage orders, and more.

# Features

### Shop admin
* Navigate through the shops list. ✅
* Make a search by title. ✅
* Edit everything except shop id. ✅
* Upload image as shop pic. ✅

### Product admin
* Navigate through product list. ✅
* Search by id or product title. ✅
* Edit everything except product id. ✅
* First image should be displayed as main image in both list view and product view. ✅
* Sort products in product list by number of orders and by price. ✅
* Filter list of products by active flag. ✅
* Filter by price range. ✅
* Attach product to one or more categories. ✅

### Category admin
* Navigate through categories list. ✅
* Search by product id, title and parent category. ✅
* Add one or more parent categories. ✅
* Display all possible paths to chosen category. ✅

### Management

* Moderation for products. ✅
* Moderation of all available pages. ✅

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
<img src=
"https://i.ibb.co/Fwk8cCt/Screenshot-2.png"
         alt="Main Page">

* Logout page

<img src=
"https://i.ibb.co/NxR9wGx/Screenshot-3.png"
         alt="Main Page">

* Product list


## Technologies Used

* Python Django
* PostgreSQL
* Pillow
* Psycopg2
* Django admin soft dashboard

## Contributors

* Jasur

## License

* MIT License

