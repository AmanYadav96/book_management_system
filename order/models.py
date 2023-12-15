from django.db import models
import uuid
from user.models import User
from book.models import Book

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False) 
    user_id = models.ForeignKey(User, default=uuid.uuid4(), on_delete = models.CASCADE)
    book_id = models.ForeignKey(Book,default=uuid.uuid4(), on_delete=models.CASCADE)
    # address_id = models.ForeignKey(Address,default=uuid.uuid4, on_delete=models.CASCADE)
    amount = models.FloatField()
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now=True)
    delivery_date = models.DateField(auto_now_add=True+7)
    delivery_time = models.TimeField(auto_now=True)
    


