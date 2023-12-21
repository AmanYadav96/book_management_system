from django.db import models
import uuid
from user.models import User
from book.models import Book
class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user_id = models.ForeignKey(User, default=uuid.uuid4(), on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, default=uuid.uuid4(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)