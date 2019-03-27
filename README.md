## What is *django_urls*?

It is flask style urls for django. 

## How to use it?

````python
# app/urls.py or where-ever you want really.
from django_urls import UrlManager
app_urls = UrlManager(views_root='dotted.path.to.app.views.module')
````

````python
# app/views/foo.py

from app.urls import app_urls

@app_urls.path('path/', name='MyView')
class MyView(View):
    ...
    
@app_urls.re_path('path2/', name='my_view')
def my_view(request):
    ...    
````

````python
# project/urls.py
from django.urls import include, path
from app.urls import app_urls

url_patterns = [
    path('some_path/', include(app_urls.url_patterns))
]
````


That's it, not too much setup, right?
