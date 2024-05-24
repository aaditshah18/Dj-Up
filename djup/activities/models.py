from django.db import models
from members.models import Members
from offers.models import Offers


class Transactions(models.Model):
    transaction_reference = models.CharField(max_length=15, unique=True, db_index=True)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, db_index=True)
    offer_id = models.ForeignKey(Offers, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transaction_reference
