# example/urls.py
from django.urls import path

from starterthree.views import index

from starterthree.views import about

from starterthree.views import me

from starterthree.views import blog

from starterthree.views import remove_account

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),

    path('remove-account', remove_account, name='remove_account'),
]