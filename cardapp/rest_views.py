from rest_framework.viewsets import ModelViewSet
from cardapp.models import Card
from cardapp.serializers import CardSerializer
# Create your views here.

class CardViewSet(ModelViewSet):
  queryset = Card.objects.all()
  serializer_class = CardSerializer