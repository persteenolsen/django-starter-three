from django.db import models

class Post(models.Model):
    
    title = models.CharField(max_length=125)
    
    # This field was added when the program was already in use and in production
    author = models.CharField(max_length=125,default='Admin')

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title