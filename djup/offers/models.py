from django.db import models


class Offers(models.Model):
    OFFER_STATUS_LAUNCHED = 'L'
    OFFER_STATUS_PLANNING = 'P'
    OFFER_STATUS_TERMINATED = 'T'

    OFFER_STATUS_CHOICES = [
        (OFFER_STATUS_LAUNCHED, 'Launched'),
        (OFFER_STATUS_PLANNING, 'Planning'),
        (OFFER_STATUS_TERMINATED, 'Terminated'),
    ]

    offer_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    status = models.CharField(
        max_length=1,
        choices=OFFER_STATUS_CHOICES,
        default=OFFER_STATUS_PLANNING,
    )
    start_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
