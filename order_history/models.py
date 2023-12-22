from django.db import models
from user.models import User
from order.models import Order
from address.models import Address
import uuid

class OrderHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, default=uuid.uuid4, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, default=uuid.uuid4, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, default=uuid.uuid4, on_delete=models.CASCADE)