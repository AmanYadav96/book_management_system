from django.db import models
import uuid

class Author(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=225)
    author_email = models.EmailField(max_length=225)
    author_number  = models.CharField(max_length=10)
    birth_date = models.DateField()
    death_date = models.DateField()
    country = models.CharField(max_length=225)
    bio = models.CharField(max_length=500)
    gender = models.CharField(max_length = 50, choices=(('Male', 'Male'),('Female','Female')))
    
    
    