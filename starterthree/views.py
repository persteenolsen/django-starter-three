from django.http import HttpResponse
from datetime import datetime

from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def me(request):
  template = loader.get_template('me.html')
  return HttpResponse(template.render())

# Working with models
from django.shortcuts import render
from .models import Post

def blog(request):
    
    # 06-08-2025 - The below statement is equal to the SQL:
    # Select * from Post order by created_at DESC
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog.html', {'posts': posts})

# 18-08-2025 - Set Account Inactive / Delete Account
from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Deactivate Account 
@login_required
@require_http_methods(['POST'])
def remove_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).update(is_active=False)
    
    # Return HTTP response to home page
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# Delete Account
'''@login_required
@require_http_methods(['POST'])
def delete_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).delete()

    # Return HTTP response to home page
    template = loader.get_template('index.html')
    return HttpResponse(template.render()) 
'''    