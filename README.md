# Restaurant Django Web App

A Django-based web application for restaurant management and operations.

## Overview

This project is built with Django and provides a comprehensive web application for managing restaurant operations. The application is composed primarily of Python backend code with HTML templates for the frontend.

## Technology Stack

- **Backend**: Python, Django
- **Frontend**: HTML
- **Deployment**: Configured with Procfile for cloud deployment

## Project Structure

```
restaurant-django-web-app/
├── Python (78.3%)          - Backend application code
├── HTML (21.3%)            - Frontend templates
└── Procfile (0.4%)         - Deployment configuration
```

## Getting Started

### Prerequisites

- Python 3.x
- Django
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ramaalmubiru-tech/restaurant-django-web-app.git
   cd restaurant-django-web-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`

## Features

- Restaurant management functionality
- Django admin interface
- HTML-based frontend templates
- Production-ready deployment configuration

## Deployment

This project includes a Procfile for easy deployment to cloud platforms such as Heroku.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Author

Created by ramaalmubiru-tech

---

For more information or support, please open an issue in the repository.
