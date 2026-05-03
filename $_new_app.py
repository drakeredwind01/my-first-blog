{new_app_name}


.yaml
new_app_name: payments
project_name: mysite


python manage.py startapp {new_app_name}



touch {new_app_name}/__init__.py
mkdir -p {new_app_name}/static/css/


touch {new_app_name}/icons/


in {project_name}/settings.py
find "INSTALLED_APPS = ["
before "]"
insert "    '{new_app_name}.apps.{new_app_name}Config',                     # app {new_app_name}
"






touch {new_app_name}/urls.py
insert "

# payments/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]

"





views.py
insert "
# {new_app_name}/views.py
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
"




mkdir -p {new_app_name}/templates/{new_app_name}/
touch {new_app_name}/templates/{new_app_name}/home.html
insert "

"





settings.py
find "TEMPLATES = ["
if not than add  "'DIRS': ['templates'],"





pip install stripe==5.5.0




User Flow
Create Checkout Session














