# Django Fundamentals

The source code for the Tuts+ series Django Fundamentals

## Setup

1. Create a virtual environment for the course and install Django (this course was created with v1.5, so it will definitely work with that version, but all bets are off on future versions of Django).

        % mkvirtualenv intermediate_django
        % pip install django

2. Get the [source code][source] for the course

        % git clone https://github.com/croach/intermediate-django.git

3. Setup the database

        % cd intermediate-django
        % manage.py syncdb         # make sure you setup an admin user
        % python loader.py         # populate DB with stories from HN

4. Run it

        % manage.py runserver


[source]: https://github.com/croach/intermediate-django/archive/master.zip
