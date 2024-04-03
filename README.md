# UnicalExpress test for Python developer 

This document provides a description and requirements for the test task for Python/Django Developer position applicants.

## Task Goal
The goal of this test task is to develop a simple Django admin panel with multi-role support for managing the content of an online store.

## Domain Description
The following image represents the class diagram that should be considered during the development of your admin panel. These are the minimal requirements for classes and fields that we expect you to add. You are free to make your own updates and add additional functionality. All image fields should be represented as links to images. You can choose any suitable database for the project.

![Class diagram](https://hb.bizmrg.com/kazanexpress/class_diagram.png)

## Requirements

### Shop Admin
1. Navigate through the list of shops.
2. Search for a shop by title.
3. Edit all fields except the shop ID.
4. Upload an image as the shop's picture.

### Product Admin
1. Navigate through the list of products.
2. Search for a product by ID or title.
3. Edit all fields except the product ID.
4. Display the first image as the main image in both the list view and the product view.
5. Sort products in the product list by the number of orders and by price.
6. Filter the list of products by the active flag.
7. Filter the list of products by price range.
8. Attach a product to one or more categories.

### Category Admin
1. Navigate through the list of categories.
2. Search for a category by product ID, title, or parent category.
3. Add one or more parent categories.
4. Display all possible paths to the chosen category.

### Management
There should be at least two administrative roles for the following purposes:
1. Moderation of products.
2. Moderation of all available pages.

## Technical Details

### Prerequisites
- Python 3.x
- Django
- Database (PostgreSQL)

### Installation
1. Clone the repository: `git clone https://github.com/karrvel/Python-task-Unical.git`
2. Change to the project directory: `cd Python-task-Unical`
3. Install the required dependencies: `pip install -r requirements.txt`

### Configuration
1. Rename the `example.env` file to `.env`.
2. Update the database configuration in the `.env` file.

### Running the Application
1. Apply database migrations: `python manage.py migrate`
2. Start the development server: `python manage.py runserver`
3. Access the admin panel in your web browser at `http://localhost:8000/admin`


## Submission
To complete the task, follow these steps:
1. Fork this repository.
2. Develop your solution.
3. Write documentation.
4. Make a pull request.

Good luck!
