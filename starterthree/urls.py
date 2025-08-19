# example/urls.py
from django.urls import path

from starterthree.views import index

from starterthree.views import about

from starterthree.views import me

from starterthree.views import blog

# 19-08-2025 - A User can not Activate own deactivate Account
# from starterthree.views import activate_account

from starterthree.views import deactivate_account

from starterthree.views import delete_account

urlpatterns = [
    
    path('', index),
    
    path('about', about),

    path('me', me),

    path('blog', blog),
    
    # 19-08-2025 - A User can not Activate own deactivate Account
    # path('activate-account', activate_account, name='activate_account'),

    path('deactivate-account', deactivate_account, name='deactivate_account'),
    
    path('delete-account', delete_account, name='delete_account'),
]