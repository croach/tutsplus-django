# Tuts+ Django Series

The source code for the Tuts+ series Django Fundamentals
=======
This is the source code for the Tuts+ series of courses on Django. The `master` branch holds the code in it's final position, i.e., as it was at the end of the last episode in the latest course in the series. The other branches are named for the course they represent and hold the code as it was at the end of that particular course. Tags have also been added to allow you to checkout the source as it was at the end of a particular episode.

## Django Unchained

The source code for the Tuts+ course "Django Unchained"

### Setup

1. Create a virtual environment for the course and install Django (this course was created with v1.5, so it will definitely work with that version, but all bets are off on future versions of Django).

        % mkvirtualenv tutsplus-django
        % pip install django

2. Get the [source code][source] for the course

    a. Clone the repository

        % git clone https://github.com/croach/tutsplus-django.git
        % cd tutsplus-django

    b. (optional) Checkout the source for a specific course or episode

        % git tag                    # list all tags (one per episode)
        % git branch -a              # list all branches (one per course)
        % git checkout <branch|tag>  # branches are by course, tags by episode

3. Setup the database

        % manage.py syncdb         # make sure you setup an admin user
        % python loader.py         # populate DB with stories from HN

4. Run it

        % manage.py runserver


[source]: https://github.com/croach/intermediate-django/archive/master.zip
