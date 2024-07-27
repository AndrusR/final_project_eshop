# Ship Happens

Ship Happens is a Django-based e-commerce website for browsing and buying motorboats, yachts, accessories, and safety equipment. The platform makes it easy to browse products, add them to your cart, and complete purchases. It also includes a real-time weather widget to help you plan your boating trips and leasing conditions page.

#### Main page of the ecommerce website![Screenshot 2024-07-27 at 15 24 36](https://github.com/user-attachments/assets/33fdd31c-c1ec-47e8-bcb3-753b036db25f)


## Features

- Browse a wide range of boats, yachts, accessories, safety equipment
- Access detailed product information and product list view
- Add and remove items in your shopping cart
- Place an order through your shopping cart
- About and Contact page of the company
- Features for login, logout and signup
- Real-time weather widget to plan your boating experience

## CMS (Content Management System)
The site has an admin panel you can access at `admin/`, where you can perform all CRUD (Create, Read, Update, Delete) operations. This makes managing content and user data straightforward and efficient.

## Built With
- Hypertext Markup Language (HTML)
- Cascading Style Sheets (CSS)
- PostgreSQL
- Docker
- Python

## Installation and Usage (Windows)

### Docker Installation (Recommended)

Make sure Docker is installed on your system.

1. **Clone the repository:**
    ```sh
    git clone https://github.com/AndrusR/final_project_eshop.git
    cd final_project_eshop
    ```

2. **Build the Docker image:**
    ```sh
    docker build --tag final_project_eshop
    ```

3. **Run the Docker container:**
    ```sh
    docker run -d -p 8000:8000 final_project_eshop
    ```

4. **Access the application:**
    Navigate to `http://127.0.0.1:8000` or `http://localhost:8000` in your browser.

### Local Installation

1. **Clone the repository and create your virtual environment:**
    ```sh
    git clone https://github.com/AndrusR/final_project_eshop.git
    cd final_project_eshop
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install the requirements:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser for admin access:**
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the application:**
    ```sh
    python manage.py runserver
    ```

6. **Visit the application:**
    Open `http://127.0.0.1:8000` or `http://localhost:8000` in your browser.

## Database

The project uses PostgreSQL for local database.

## Testing

Execute tests with the following command:
```sh
pytest tests
```

## GIT

- Each new branch should be created from the `main` branch.
- For the branch naming, start each branch name with the prefix according to the work you intend to do in it:
  - feature/
- For the merge request, target the working branch to the master branch.
