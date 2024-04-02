# Online Store Admin Panel Documentation

## Welcome to the documentation for the Online Store Admin Panel. This admin panel is designed to manage the content for an online store with multi-role support. Below you will find information on how to navigate through the admin panel, perform various tasks, and understand the functionalities provided.



## To get started with the Online Store Admin Panel, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies (Django, etc.).
3. Set up your database (SQLite, MySQL, etc.).
4. Run the Django migrations to create the necessary tables.
5. Start the Django development server.
6. Access the admin panel through your web browser.

## Features
The Online Store Admin Panel provides the following features:

1. Management of shops, products, and categories.
2. Search functionality for shops and products.
3. Editing of shop and product details.
4. Image upload for shop picture.
5. Sorting products by number of orders and price.
6. Filtering products by active flag and price range.
7. Attachment of products to one or more categories.
8. Multi-role support with administrative roles for moderation.

## Usage
Shop Admin

1. Navigate through the list of shops.
2. Search for shops by title.
3. Edit shop details except for shop ID.
4. Upload an image as a shop picture.

Product Admin
1. Browse the list of products.
2. Search for products by ID or title.
3. Edit product details except for product ID.
4. Display the first image as the main image in list view and product view.
5. Sort products by number of orders and price.
6. Filter products by active flag and price range.
7. Attach products to one or more categories.

Category Admin
1. View the list of categories.
2. Search for categories by product ID, title, or parent category.
3. Add one or more parent categories.
4. Display all possible paths to the chosen category.

## Management Roles
The admin panel supports two administrative roles:

1. Moderation for Products: Allows moderation of products, including approval or rejection.
2. Moderation of Pages: Allows moderation of all available pages in the admin panel.