from django.db import models
import uuid
from user.models import User

class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    user_id = models.ForeignKey(User, default=uuid.uuid4, on_delete= models.CASCADE)
    city = models.CharField(max_length=225)
    pincode = models.CharField(max_length=6)
    state = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    address = models.CharField(max_length=500)
    address_type = models.CharField(max_length = 50, choices=(('Home', 'Home'),('Office','Office')))
    created_at = models.DateTimeField(auto_now_add=True)
