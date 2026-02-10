
# quick start
venv\Scripts\activate


# commit
pip freeze > requirements.txt
git add .
git commit -m "base django setup"
git push






# create venv

> python -m venv venv # windows

# Working with virtualenv
venv\Scripts\activate # activate

# Installing Django
## install/upgrade pip
python -m pip install --upgrade pip

make requirements.txt
put in Django~=5.1.2

pip install -r requirements.txt

# Install Git




# Your first Django project!

On Windows you should run the following command. (Don't forget to add the period (or dot) . at the end):

command-line
(myvenv) C:\Users\Name\djangogirls> django-admin.exe startproject mysite .


# create superuser
python manage.py createsuperuser
http://127.0.0.1:8000/admin/




# extention
1. Markdown Decorations (Highly Recommended)
This is the most direct answer to your request. It applies styles like bolding and italics to the text inside the editor while leaving the syntax markers visible.

What it does: It bolds headers, italicizes _text_, and bolds **text** without hiding the symbols. It also adds background colors to code blocks and blockquotes.

Why it's great: It doesn't change the editor's behavior; it just makes the code look like the final result.

How to get it: Search for "Markdown Decorations" by remcohaszing in the Extensions marketplace.



# Changing the Timezone
[Wikipedia's list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
America/Los_Angeles

### mysite/settings.py
TIME_ZONE = 'America/Los_Angeles'

### mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Starting the web server
(venv) ~\djangogirls> python manage.py runserver
    if doesn't work
(venv) ~\djangogirls> python manage.py runserver 0:8000

### browser
http://127.0.0.1:8000/

### browser
http://127.0.0.1:8000/admin




# Creating an application
python manage.py startapp blog


# tell Django that it should use new application (e.g. newapp, blog)
mysite/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newapp',
    'blog',
]






# Pro-Tip: The "New Computer" Test
If you want to work on your project on another computer, the professional workflow is:

git clone (Download your code).

Create a fresh venv on that new computer.

Run pip install -r requirements.txt (Build your tools).


## add new model to our database
Run
python manage.py makemigrations blog (Django prepared a migration file)



python manage.py migrate (Build your database from the blueprint).



# Django admin
blog/admin.py
    from django.contrib import admin
    from .models import Post

    admin.site.register(Post)



# urls.py main
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),


# urls.py blog
from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# views.py
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})


# app(blog) > templates > blog > post_list.html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Ola's blog</title>
        </head>
        <body>
            <p>Hi there!</p>
            <p>It works!</p>

            <h1>A heading</h1> for your most important heading
            <h2>A sub-heading</h2> for a heading at the next level
            <h3>A sub-sub-heading</h3> …and so on, up to <h6>
            <p>A paragraph of text</p>
            <em>text</em> emphasizes your text
            <strong>text</strong> strongly emphasizes your text
            <br> goes to another line (you can't put anything inside br and there's no closing tag)
            <a href="https://djangogirls.org">link</a> creates a link
            <ul><li>first item</li><li>second item</li></ul> makes a list, just like this one!
            <div></div> defines a section of the page
            <nav></nav> defines a set of navigation links
            <article></article> specifies independent, self-contained content
            <section></section> defines a section in a document
            <header></header> specifies a header for a document or section
            <main></main> specifies the main content of a document
            <aside></aside> defines some content aside from the content it is placed in (like a sidebar)
            <footer></footer> defines a footer for a document or section
            <time></time> defines a specific time (or datetime)
        </body>
    </html>























# more about Django admin
https://docs.djangoproject.com/en/5.1/ref/contrib/admin/

