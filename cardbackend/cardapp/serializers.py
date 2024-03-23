from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from cardapp.models import Card
 
class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = [
          'id', 'number', 'name_of_owner', 
          'email_of_owner', 'phone', 'credit', 'type_of_card'
        ]