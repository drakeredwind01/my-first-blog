
command-line
$ git status
$ git add .
$ git status
$ git commit -m "Added view and template for detailed blog post as well as CSS for the site."
$ git push



Then, in a PythonAnywhere Bash console:

PythonAnywhere command-line
$ cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
$ git pull
[...]



$ workon drakeredwind01.pythonanywhere.com
$ python manage.py collectstatic
or 
$ python manage.py collectstatic --noinput
[...]

click the Reload button on the Web tab
