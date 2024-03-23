from django.db import models

# Create your models here.
class Card (models.Model):
  """
  Represents a model of a single credit card
  """
  VISA = "VISA"
  MASTERCARD = "MASTERCARD"
  AMEX = "AMEX"
  TYPE_OF_CARDS = (
      (VISA, "Visa"),
      (MASTERCARD, "Mastercard"),
      (AMEX, "Amex")
  )
  number = models.IntegerField(null=True, blank=True, verbose_name="Numero")
  credit = models.DecimalField(
        "Credito Total", default=0.00, max_digits=12, decimal_places=2, 
        null=True, blank=True)
  name_of_owner = models.CharField("Nombres", max_length=120)
  email_of_owner = models.CharField("Email", max_length=120)
  phone = models.CharField("Telefono", max_length=20, null=True, blank=True)
  type_of_card = models.CharField(
        "Tipo de documento", max_length=10, choices=TYPE_OF_CARDS, 
        default=VISA)
  
  def __str__(self):
      return self.name_of_owner
  
  class Meta:
      verbose_name = 'Card'
      verbose_name_plural = 'Cards'
      db_table = 'card'
      ordering = ['id']
  
