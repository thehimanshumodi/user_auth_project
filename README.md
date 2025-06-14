# User Authentication and Dashboard Application

This project is a web application built with Django that provides user signup and login functionalities, supporting two distinct user types: **Patient** and **Doctor**. Upon successful login, users are redirected to their respective dashboards, which display their registered details.

## Features

* **User Types:** Supports `Patient` and `Doctor` user roles.
* **Secure Signup:** Users can create new accounts with the following fields:
    * First Name
    * Last Name
    * Profile Picture (image upload)
    * Username
    * Email Id
    * Password (hashed for security)
    * Confirm Password (with client-side and server-side matching validation)
    * Address (Line 1, City, State, Pincode)
* **User Login:** Authenticates users based on username and password.
* **Role-Based Redirection:** Automatically redirects users to their specific dashboards (`/dashboard/patient/` or `/dashboard/doctor/`) after login.
* **User Dashboards:** Simple dashboards displaying the user's registered information and profile picture.
* **Logout Functionality:** Allows users to securely log out of their accounts.
* **Password Hashing:** Passwords are automatically hashed and salted using Django's built-in security features.
* **CSRF Protection:** Built-in Cross-Site Request Forgery protection for all forms.

## Technology Stack

* **Backend:** Python 3.x, Django 5.x
* **Database:** SQLite (default for development)
* **Frontend:** HTML, CSS

## Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **pip** (Python package installer)

## Installation and Setup

Follow these steps to set up and run the project locally:

1.  **Create Project Directory and Initialize:**

    ```bash
    mkdir user_auth_project
    cd user_auth_project
    ```

2.  **Set up a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install Django and Pillow (for image handling).

    ```bash
    pip install Django Pillow
    ```

4.  **Create Django Project and App Structure:**
    Create the main Django project and an `accounts` app within it.

    ```bash
    django-admin startproject user_auth_project .
    python manage.py startapp accounts
    ```

5.  **Copy Files:**
    Place the provided code into the respective files and directories:

    * `user_auth_project/settings.py`
    * `user_auth_project/urls.py`
    * `accounts/models.py`
    * `accounts/forms.py` (create this file)
    * `accounts/views.py`
    * `accounts/urls.py` (create this file)
    * `accounts/templates/accounts/base.html` (create directory `accounts/templates/accounts/` first)
    * `accounts/templates/accounts/signup.html`
    * `accounts/templates/accounts/login.html`
    * `accounts/templates/accounts/patient_dashboard.html`
    * `accounts/templates/accounts/doctor_dashboard.html`

6.  **Update `settings.py`:**
    * Add `'accounts'` to `INSTALLED_APPS`.
    * Set `AUTH_USER_MODEL = 'accounts.CustomUser'`.
    * Configure `MEDIA_URL` and `MEDIA_ROOT` for profile picture uploads:
        ```python
        # user_auth_project/settings.py
        import os

        # ... other settings ...

        INSTALLED_APPS = [
            # ...
            'accounts',
        ]

        AUTH_USER_MODEL = 'accounts.CustomUser'

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        ```

7.  **Update `urls.py` (Project Level):**
    Include the `accounts` app's URLs and configure serving media files in development.

    ```python
    # user_auth_project/urls.py
    from django.contrib import admin
    from django.urls import path, include
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('accounts.urls')), # Include app's URLs
    ]

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

8.  **Make Migrations:**
    Create the database tables for the `CustomUser` model.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9.  **Create Media Directory:**
    Manually create a `media` directory in the root of your `user_auth_project` where profile pictures will be stored.

    ```bash
    mkdir media
    ```

10. **Optional: Create a Default Profile Picture:**
    If you want a default image when no profile picture is uploaded, create an `accounts/static/` directory and place an image named `default_profile.png` inside it. Then, ensure `accounts` app's static files are configured in `settings.py` (which Django usually handles by default for `static` directories inside apps).

11. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1.  **Access the Application:**
    Open your web browser and go to `http://127.0.0.1:8000/`. You will be redirected to the login page.

2.  **Signup:**
    * Click on "Sign Up here" or navigate to `http://127.0.0.1:8000/signup/`.
    * Fill in all the required details, including first name, last name, username, email, password, confirm password, address, and select a user type (Patient or Doctor).
    * You can optionally upload a profile picture.
    * Ensure "Password" and "Confirm Password" match.
    * Click "Sign Up". You will receive a success message and be redirected to the login page.

3.  **Login:**
    * On the login page (`http://127.0.0.1:8000/login/`), enter your registered username and password.
    * Click "Login".
    * Upon successful login, you will be redirected to your respective dashboard:
        * **Patient:** `http://127.0.0.1:8000/dashboard/patient/`
        * **Doctor:** `http://127.0.0.1:8000/dashboard/doctor/`
    * Your dashboard will display the details you entered during signup.

4.  **Logout:**
    * On any dashboard page, click the "Logout" button to end your session. You will be redirected to the login page.
