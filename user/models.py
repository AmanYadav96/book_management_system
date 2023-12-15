from django.db import models
import uuid
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=225)
    user_email = models.EmailField(max_length=225)
    user_number = models.CharField(max_length=10)
    username = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    is_verify = models.BooleanField(default=False)