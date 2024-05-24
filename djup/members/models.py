from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=50, db_index=True, blank=True, null=True)
    mobile = models.CharField(max_length=15, db_index=True, blank=True, null=True)
    member_id = models.CharField(max_length=15, db_index=True, unique=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
