## Setting Up the Project

### Setting Up the Project via Virtual Environment

1. Install project requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements/develop.txt
   ```

2. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```
   Modify `DJANGO_SETTINGS_MODULE` to `config.settings.develop` and `DB_HOST` to `localhost` in the `.env` file.

3. Create the database:
   ```bash
   sudo -u postgres psql
   CREATE DATABASE python_task_unical;
   ```

   If you prefer not to use the `postgres` user, create a new user and grant all privileges:
   ```bash
   CREATE USER my_user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE my_user TO python_task_unical;
   ```

4. Set up the `.env` file with your database credentials:
   ```bash
   nano .env
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Load default data:
   ```bash
   python manage.py loaddata data.json
   ```

7. Load media files:
   ```bash
   unzip media.zip
   ```

8. Run the server:
   ```bash
   python manage.py runserver
   ```

## Setting Up with Docker

1. Create a `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Load media files:
   ```bash
   unzip media.zip
   ```

3. Build and run Docker:
   ```bash
   docker-compose up --build
   ```

4. Load default data:
   ```bash
   docker exec -it PYTHON_TASK_UNICAL_backend /bin/sh
   ```
   Then execute:
   ```bash
   python manage.py loaddata data.json
   ```
   Restart Docker.

5. Open a browser and go to `http://localhost:8000/`. Use the following superuser credentials: `admin`/`admin`.

### Additional Steps
- **Recaptcha:**

  You can get key for recaptcha from [here](https://www.google.com/recaptcha/admin/create) and add it to the `.env`
  file. Then add keys to the `.env` file:
  ```bash
  RECAPTCHA_SITE_KEY=your_site_key
  RECAPTCHA_SECRET_KEY=your_secret_key
  ```

- **Pre-commit Hook:**

  Install and configure pre-commit hook:
  ```bash
  pip install pre-commit
  pre-commit install
  ```

- **Running Tests:**
  Execute tests with the following command:
  ```bash
  python manage.py test
  ```

---
[Task Description](task_description.md)

Here is the additional update made to the models:

- **User Model:**
    - **Shop:** This field allows associating a user with a particular shop, facilitating management and ownership
      within the system.


- **Category Model:**
    - **Order:** This field allows changing the sequence of categories.
    - **Icon:** Added for better visual representation of categories.

- **Product Image Model:**
    - **Order:** This field facilitates reordering images associated with a product.
    - **Is Main:** This addition allows specifying one image as the main picture for a product.

## Existing User Roles

1. **Super User:**
    - Has unrestricted access and control over the entire system.

2. **Guest:**
    - Has read-only access to the system.

3. **Moderator:**
    - Responsible for moderating all items within the system.

4. **Product Moderator:**
    - Manages product listings across the system.

5. **Shop Owner:**
    - Manages shop information and products within their respective shops.

6. **Shop Product Moderator:**
    - Manages only the products associated with a specific shop.
