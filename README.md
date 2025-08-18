

# Python + Django + MySQL + Membership System + Vercel

This example shows how to use Django 5.1.11 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

Last updated: 18-08-2025

Node version selected at Vercel Cloud: 22

## Demo at Vercel

https://django-starter-three.vercel.app/

## Installing

- Download Python from the official website [Python](https://python.org/)
- Make sure that you have installed Python by the command in Powershell: "python --version"
- Download the Python extension for Visual Studio Code which automatically include the Pylance extionsion
- Download / fork this Django Starter Website from my GitHub
- Create the virtual envirement ".venv" for the Django Web App by Powershell or by VS Code
- Virtual Enviroment by VS Code: "View - Command Palette - Python Create Enviroment"


The Administration Backend can use MySQL for Dev + Prod but can also work with a SQLite DB for developement locally ( Dev )

## How it Works

Our Django application, `starterthree` is configured as an installed application in `vercel_app/settings.py`:

```bash
# vercel_app/settings.py
INSTALLED_APPS = [
    # ...
    'starterthree',
]
```

We allow "\*.vercel.app" subdomains in `ALLOWED_HOSTS`, in addition to 127.0.0.1:

```bash
# vercel_app/settings.py
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

The `wsgi` module must use a public variable named `app` to expose the WSGI application:

```bash
# vercel_app/wsgi.py
app = get_wsgi_application()
```

The corresponding `WSGI_APPLICATION` setting is configured to use the `app` variable from the `vercel_app.wsgi` module:

```bash
# vercel_app/settings.py
WSGI_APPLICATION = 'vercel_app.wsgi.app'
```

This Django example uses the Web Server Gateway Interface (WSGI) with Django to enable handling requests on Vercel with Serverless Functions.

## Routing 

There are severals views in `starterthree/views.py` which load HTML Django Templates `templates`:

The views are exposed a URL through `starterthree/urls.py`:

```bash
# example/urls.py
from django.urls import path

from starterthree.views import index
from starterthree.views import about
from starterthree.views import me

urlpatterns = [
    path('', index),
    path('about', about),
    path('me', me),
]
```
Finally, it's made accessible to the Django server inside `vercel_app/urls.py`:

```bash
# vercel_app/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('example.urls')),
]
```

## Templates

To use templates create the dir 'templates' at root level and put the HTML files there

There is only one Django App in the Project and the dir 'templates' can be at root level

Tell Django where to look for Templates by `starterthree/settings.py`:

Find the section TEMPLATES = [] and add the dir of the Templates

'DIRS': [BASE_DIR / 'templates']

## Running Locally

```bash
python manage.py runserver
```
Your Django application is now available at `http://127.0.0.1:8000/`.

## The Admin Backend and Databases

The Admin Backend is using a MySQL Database for both Dev + Prod, but is able to use a SQLite for Dev

To connect to the MySQL install the Python package "pymysql" and the packages from the requirements.txt

```bash
pip install -r requirements.txt
```

Take a look at the files needed for connecting to MySQL: `vercel_app/mysql_setup.py` and 

`vercel_app/__init__.py`

Create a Super User for the Admin Backend in the MySQL

```bash
python manage.py createsuperuser
```

Make the Migration to the MySQL DB

```bash
python manage.py makemigrations
python manage.py migrate
```
You will need to do the Migration at first and when / if you will add, update or delete models.py which this Django Web App does not use

For using a SQLite developing / locally make the config in the setting file `vercel_app/settings.py`

Find the section DATABASES = {} and add support for SQLite and comment out the MySQL

## Static files for the Admin Backend and the Frontend

There is only one Django App in the Project and the dir 'static' and 'assets' can be created at root level

Make sure that the Python package 'whitenoise' is installed from the requirements.txt

Note: Make sure you have the line 'whitenoise.middleware.WhiteNoiseMiddleware' in the 

MIDDLEWARE = [] at the `vercel_app/settings.py` along with the other packages

Finally, take a look at `vercel_app/settings.py`:

Find where Django now looks for the static files

STATIC_URL = 'static/'

Where you put your static files in the dir 'static'

STATIC_ROOT = BASE_DIR/'static' 

## Additional directory from which to load static files if wanted

The files in the dir 'asset' will be copied to the dir 'static' after running

```bash
python manage.py collectstatic
```

The static files for the Admin Backend will also be created in the dir 'static' by the above command

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'assets')
]

## Check that Django is serving static files by URL

Type the URL in your Browser after deployment to Vercel

https:// your project at vercel.app/static/pso-django.jpg

or the URL when running locally

`http://127.0.0.1:8000/static/pso-django.jpg`

If everything is fine my photo will be displayed

The CSS files can be tested the same way like the .jpg above

Now you can use the images and CSS in your Templates

## Running Locally and take a look at the Admin Backend

```bash
python manage.py runserver
```

The Django application is now available at `http://127.0.0.1:8000/admin`

## Deployment to Vercel

Make sure that your static files are ready by running

```bash
python manage.py collectstatic
```

Take a look at the file `vercel.json`

Make sure to set Debug = False in the file `vercel_app/settings.py`

Make a commit to your GitHub and your Django will build and deploy

## Models

Add a simple Model "Post" to be administrated by the Admin Backend and displayed by the Frontend

- Create a file `starterthree/models.py` with your new Model Post

- Make a regitration of your Model in `starterthree/admin.py`

- Create the View for handling the Posts `starterthree/views.py`

- Add the view / template blog in `starterthree/urls.py`

- Create a Template for display the Posts `templates/blog.html`

- Create a folder with the path: `starterthree/migrations` and run the command:

```bash
python manage.py makemigrations starterthree
```
Note: It is important to add the name of the app in the command `starterthree` !!!

This command will create a file for the migration of the Model to a Table in the MySQL DB

- Now run the command: 

```bash
python manage.py migrate
```
This will create the Table Post in the DB and you are now ready for administrate the Posts by the Django Admin Backend

# Membership System

A Membership System by django-allauth package with the below features:

- Signup with Email Verification

- Login

- Logout

- Reset Password

- Change Password when logged in

- Manage Email when logged in

- Deactivate own Account when logged in

For implementing the Membership System take a look at the Documentation by django-allauth and this Starter where the following files are involved:

- requirements.txt

- .env

- vercel_app / settings

- vercel_app / urls

- templates

- templates / account

- templates / allauth / layouts

- Both the SQLite + MySQL DB

Happy use of Django :-)
