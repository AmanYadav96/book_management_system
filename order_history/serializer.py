from rest_framework import serializers
from order_history.models import OrderHistory

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = OrderHistory
        fields = '__all__'
