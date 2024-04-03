<h1><strong>Simple Django Admin Panel for Online Store Management</strong></h1>

<p>This project aims to develop a simple Django admin panel for managing the content of an online store with multi-role support. The admin panel allows administrators to efficiently manage shops, products, categories, and administrative roles.</p>

<h2><strong>Stacks:</strong></h2>

<p>The project is built using the following technologies:</p>

<ul>
  <li>Django 5.0.3</li>
  <li>django-better-admin-arrayfield 1.4.2</li>
  <li>django-js-asset 2.2.0</li>
  <li>django-mptt 0.16.0</li>
  <li>asgiref 3.8.1</li>
  <li>pillow 10.3.0</li>
  <li>psycopg2-binary 2.9.9</li>
  <li>sqlparse 0.4.4</li>
  <li>typing_extensions 4.10.0</li>
</ul>

<h2><strong>Features:</strong></h2>

<ul>
  <li><strong>Shop Administration:</strong>
    <ul>
      <li>Navigate through the list of shops.</li>
      <li>Search shops by title.</li>
      <li>Edit shop details except for the shop ID.</li>
      <li>Upload images as shop pictures.</li>
    </ul>
  </li>

  <li><strong>Product Administration:</strong>
    <ul>
      <li>Navigate through the list of products.</li>
      <li>Search products by ID or title.</li>
      <li>Edit product details except for the product ID.</li>
      <li>Display the first image as the main image in both list and product view.</li>
      <li>Sort products by the number of orders and price.</li>
      <li>Filter products by active flag and price range.</li>
      <li>Attach products to one or more categories.</li>
    </ul>
  </li>

  <li><strong>Category Administration:</strong>
    <ul>
      <li>Navigate through the list of categories.</li>
      <li>Search categories by product ID, title, and parent category.</li>
      <li>Add one or more parent categories to a category.</li>
      <li>Display all possible paths to the chosen category.</li>
    </ul>
  </li>

  <li><strong>Management:</strong>
    <ul>
      <li>Define at least two administrative roles:
        <ul>
          <li>Moderation for products.</li>
          <li>Moderation for all available pages.</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>

<h2><strong>Additional Functionalities:</strong></h2>

<ul>
  <li>Extensive documentation provided for better understanding and usage of the admin panel.</li>
  <li>Customizable user interface to enhance user experience.</li>
  <li>Integration with authentication systems for secure access.</li>
  <li>Support for multiple languages and internationalization.</li>
  <li>Implementation of data validation and error handling mechanisms.</li>
  <li>Compatibility with various databases for flexible deployment options.</li>
</ul>

<h2><strong>How to Use:</strong></h2>

<ol>
  <li>Fork or clone this repository.</li>
  <li>Set up the Django environment and install requirements.txt</li>
  <li>Configure database settings according to your preference.</li>
  <li>Here you are!</li>
</ol>
