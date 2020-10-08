# users/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models




class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ic_number = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)

    GENDER = [
        # To follow SRs
        ('NA', 'Not Available'),   
    ]

    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default='NA',
    )  

    MARITAL_STATUS = [
        # To follow SRS
        ('NA', 'Not Available'),   
    ]

    marital_status = models.CharField(
        max_length=2,
        choices=MARITAL_STATUS,
        default='NA',
    )      

    greencard_number = models.CharField(blank=True, max_length=255)
    greencard_expiry_date = models.DateTimeField(null=True)

    position = models.CharField(blank=True, max_length=255)
    role = models.CharField(blank=True, max_length=255)
    address1 = models.CharField(blank=True, max_length=255)
    address2 = models.CharField(blank=True, max_length=255)
    postcode = models.IntegerField(null=True)

    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)    

    office_number = models.CharField(blank=True, max_length=255)
    handphone_number = models.CharField(blank=True, max_length=255)
    fax_number = models.CharField(blank=True, max_length=255)
    
    picture = models.TextField(null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return self.name

class AcademicQualification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    year = models.IntegerField(null=True)
    institution = models.CharField(blank=True, max_length=255)
    program =models.CharField(blank=True, max_length=255)
    qualification = models.CharField(blank=True, max_length=255)
    created_by = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name            

class WorkExperience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    year_from = models.IntegerField(null=True)
    year_to = models.IntegerField(null=True)
    position = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=255)
    created_by = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name   

class Trainer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    trainer_number = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name          

class Assessor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    assessor_number = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name     

class UserSettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, max_length=255)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name            
