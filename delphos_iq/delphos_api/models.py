import uuid
from django.db import models


# Create your models here.
class Loans(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(db_index=True, max_length=255)
    country = models.CharField(db_index=True, max_length=50)
    sector = models.CharField(db_index=True, max_length=128)
    amount = models.CharField(db_index=True, max_length=25)

    def __str__(self):
        return f'{self.title} | {self.country} | {self.sector} | {self.amount}'

