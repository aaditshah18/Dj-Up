from django.db import models
from members.models import Members
from offers.models import Offers

class Transactions(models.Model):
    transaction_reference = models.CharField(max_length=15, unique=True, db_index=True)
    member_id = models.ForeignKey(Members, db_index=True)
    offer_id = models.ForeignKey(Offers)

