# Puddle E-commerce 🛍️

Puddle is an e-commerce platform built using Django. It allows users to browse products, add items to the cart, and place orders. Users can manage their profiles and view their order history, while admins can handle product management.

## 📝 Features

- **User Authentication**: Secure login and registration.
- **Product Listings**: Browse products by category, search, and view product details.
- **Cart Management**: Add products to the cart, modify quantities, and proceed to checkout.
- **Order System**: Users can place orders and view their order history.
- **Admin Dashboard**: Manage products, orders, categories, and users via Django's built-in admin interface.

## 🎮 How to Use

1. **Register**: Create an account to start shopping.
2. **Browse Products**: View products by category or use the search feature.
3. **Add to Cart**: Select products and add them to your shopping cart.
4. **Checkout**: Enter shipping details and proceed with payment.
5. **Order Confirmation**: View order details and track your purchases.

## 🔧 Code Overview

- **User Authentication**: 
  - `views.py`: Handles user registration, login, and profile management.
  - `models.py`: Defines user and order models.
  
- **Product Management**:
  - `Product`: Represents an item in the store.
  - `Category`: Organizes products into categories.
  
- **Cart & Checkout**:
  - `Cart`: Stores user selections before checkout.
  - `Order`: Manages user purchases and order status.
  
- **Django Admin**: Admins can manage the website's content, users, products, and orders.

## 🛠 Setup and Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Virtual Environment (optional but recommended)

### Steps to Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/puddle.git
    cd puddle
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create Superuser** (for admin panel access):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access Website**:
   Visit `http://127.0.0.1:8000` in your browser.

---

## 🎰 Functionalities

- **User Registration & Login**: 
  - Users can sign up, log in, and manage their profiles.
  
- **Product Search and Categories**: 
  - Products are searchable by name and filterable by categories.
  
- **Shopping Cart**: 
  - Users can add products to the cart, modify item quantities, and proceed to checkout.
  
- **Order History**:
  - Registered users can view and manage their orders.

## 🛍 Product Management

- **Admin Dashboard**: 
  - Admins can add, update, and delete products and categories.
  - Manage orders and update order statuses.

## ⚙️ Requirements

- Python 3.x
- Django 3.x
- Bootstrap (for frontend styling)
- SQLite (for development)
- PostgreSQL (for production)

## 📄 License

This project is licensed under the MIT License.
