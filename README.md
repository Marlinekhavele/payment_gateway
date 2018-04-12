# wallet
# payment_system
# payment
# wallet
# wallet
# bank

# Dev Setup

### Create a virtual environment for running python3
```
python3 -m venv .virtualenv
```

### Activate the virtual environment

```
source .virtualenv/bin/activate

# check python version after activation
python --version
```

### Install Dependencies

```
# make sure virtualenv is activated first
pip install -r requirements.txt
```

### Run Database Migrations
```
# run db migrations if necessary
./payment/manage.py makemigrations
./payment/manage.py migrate
```

### Create User
```
./payment/manage.py createsuperuser
```

### Collect static files
```
./payment/manage.py collectstatic
```

### Run App in Dev mode
```
./payment/manage.py runserver

# After running successfully the site is accessible via http://127.0.0.1:8000/
```

### Testing gunicorn ability to serve the project

```
# on success should be able to serve the app
gunicorn --pythonpath payment payment.wsgi --log-file -
```

# Deploying to Heroku

### Create the app on Heroku
```
# ensure heroku cli is installed and logged in first (see heroku documentation)
heroku create
```

### Push new code to Heroku
```
git push heroku master
```

### Run migrations on Heroku
```
heroku run python ./payment/manage.py migrate
```

### Create default django user
```
heroku run python ./payment/manage.py createsuperuser
```

### Launch the application
```
heroku open
```
