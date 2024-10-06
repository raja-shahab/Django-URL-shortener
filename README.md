# Django URL Shortener

## Introduction
This Django application is a simple URL shortener. Users can input a long URL, and the application generates a short URL that redirects to the original one. It's built with Django and provides a clean interface for generating and managing short links.

## Features
- Generate shortened URLs from long URLs
- Redirect short URLs to the original URL
- Track the number of times a short URL is accessed
- Simple admin interface to manage URLs

## Configuration
To configure the application, you will need to modify the `settings.py` file, and ensure that your `ALLOWED_HOSTS` and `DATABASE` settings are properly configured for your environment.

For generating the short URL slugs, the app uses Python's `hashlib` to generate unique short codes. You can customize this in the `models.py` file.

## URL Redirection Logic
The application maps the shortened URLs to their corresponding original URLs by storing them in the database. When a user visits a short URL, the following process happens:

- Django's view checks the slug in the database.
- If the slug exists, the user is redirected to the original URL.
- If the slug doesn't exist, an error page is displayed.

## Admin Panel
You can manage all URLs through Django's admin interface. Use the following command to access the admin panel after starting the server:

    python manage.py createsuperuser  # If you haven't created an admin user
    python manage.py runserver


Then visit http://127.0.0.1:8000/admin/ to log in and manage URLs.

## Contributing

- Fork the repository.
- Create a new branch for your feature: git checkout -b feature-branch
- Make your changes and commit: git commit -m "Add new feature"
- Push to your branch: git push origin feature-branch
- Open a pull request.

## License
This project is licensed under the MIT License. 

## Query
For any query, please feel free to reach out to rajashahab912@gmail.com
