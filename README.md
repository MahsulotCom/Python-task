# 📦 Product Management

## 📝 Description

Admin panel for managing products, shops and categories.

## 📄 Features

### Shop admin
1. Navigate through the shops list.
2. Make a search by title.
3. Edit everything except shop id.
4. Upload image as shop pic. 

### Product admin
1. Navigate through product list.
2. Search by id or product title.
3. Edit everything except product id.
4. First image should be displayed as main image in both list view and product view.
5. Sort products in product list by number of orders and by price.
6. Filter list of products by active flag.
7. Filter by price range.
8. Attach product to one or more categories.

### Category admin
1. Navigate through categories list.
2. Search by product id, title and parent category.
3. Add one or more parent categories. 
4. Display all possible paths to chosen category. 

### Image admin
1. Upload images for products, shops.
2. You can upload multiple images.
3. Main image should be displayed in product/shop view.

### Management
There are two administrative roles for the following purposes:
1. Moderation for products. 
2. Moderation of all available pages. 


## 💻 Technology

| Technology            | Use                           |
| --------------------- | ----------------------------- |
| Python                | Main programming language     |
| Django                | Web framework                 |
| SQLite                | Database                      |


## 🚀 Getting Started

1. Clone the repository

    ```bash
    git clone https://github.com/ShokhrukhbekYuldoshev/Python-task.git
    ```

    ```bash
    cd your-repo
    ```


2. Run the migrations

    ```bash
    python manage.py migrate
    ```

3. Create a virtual environment

    ```bash
    python -m venv .venv
    ```

4. Install requirements

    ```bash
    pip install -r requirements.txt
    ```

5. Activate the virtual environment:

    For Linux/MacOS:

    ```bash
    source .venv/bin/activate
    ```

    For Windows:

    ```bash
    .venv\Scripts\activate
    ```

6. Run the server

    ```bash
    python manage.py runserver
    ```

7. Go to http://localhost:8000/admin    

## 🚀 Additional information

There are two groups of users:

1. Moderator: Can create, edit and delete products, shops, categories and images.
2. Product manager: Can create, edit and delete only products.

Login as moderator: username: test, password: test

Login as product manager: username: test2, password: testqwerty