from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.helpers import PathAndRename

from users.models import CustomUser, Trainer


class Application(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    training_type = models.CharField(blank=True, max_length=255)
    training_size = models.IntegerField(null=True)
    ccd_size = models.IntegerField(null=True)

    from_date = models.DateTimeField(null=True)  
    to_date = models.DateTimeField(null=True)  

    passing_mark = models.IntegerField(null=True)

    certificate_type = models.CharField(blank=True, max_length=255)

    address1 = models.CharField(blank=True, max_length=255)
    address2 = models.CharField(blank=True, max_length=255)
    postcode = models.IntegerField(null=True)

    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)   

    coach = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name

