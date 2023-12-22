from django.db import models
import uuid
from author.models import Author

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=500)
    publication_date = models.DateField()
    ISBN = models.CharField(max_length=25)
    genre = models.CharField(max_length=225)
    cover_image = models.CharField(max_length=225)
    summary = models.CharField(max_length=10000)
    price = models.FloatField()
    page_count = models.IntegerField()
    rating = models.FloatField(max_length=2)
    author = models.CharField(max_length=225)
    edition = models.BigIntegerField()
    is_available = models.BooleanField(default=False)
    is_ebook_available = models.BooleanField(default=False)


