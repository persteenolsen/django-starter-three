# example/urls.py
from django.urls import path

from starterthree.views import index

from starterthree.views import about

from starterthree.views import me

from starterthree.views import blog

from starterthree.views import deactivate_account

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

    path('deactivate-account', deactivate_account, name='deactivate_account'),
]