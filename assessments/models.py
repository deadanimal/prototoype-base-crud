from __future__ import unicode_literals 
import uuid 
from django.db import models
from django.utils.formats import get_format

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.helpers import PathAndRename

from users.models import CustomUser, Trainer, Assessor


class Assessment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE, null=True)
    application_date = models.DateTimeField(null=True)    
    proposed_date = models.DateTimeField(null=True)    
    assessment_date = models.DateTimeField(null=True)    

    status = models.CharField(blank=False, max_length=255)
    payment = models.CharField(blank=False, max_length=255)


    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class AssessmentData(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True)
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE, null=True)

    block = models.IntegerField(null=True)
    unit = models.IntegerField(null=True)
    time_ = models.DateTimeField(null=True)

    number_of_sample = models.IntegerField(null=True)
    arch_work = models.FloatField(null=True)
    floor_finishes = models.FloatField(null=True)
    internal_wall = models.FloatField(null=True)
    ceiling = models.FloatField(null=True)
    door = models.FloatField(null=True)
    window = models.FloatField(null=True)
    internal_fixtures = models.FloatField(null=True)
    roof = models.FloatField(null=True)
    external_wall = models.FloatField(null=True)
    apron_parameter_drain = models.FloatField(null=True)
    carpark_carporch = models.FloatField(null=True)
    arch_work = models.FloatField(null=True)
    material_functional_test = models.FloatField(null=True)
    total = models.FloatField(null=True)
    picture = models.TextField(null=True)
    basic_me_fittings = models.FloatField(null=True)
    qlassic_score_mockup = models.FloatField(null=True)
    qlassic_score = models.FloatField(null=True)



    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name


class Project(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, null=True)
    title = models.CharField(blank=True, max_length=255)
    classification = models.CharField(blank=True, max_length=255)
    sector = models.CharField(blank=True, max_length=255)
    building_category = models.CharField(blank=True, max_length=255)
    construction_method = models.CharField(blank=True, max_length=255)
    title = models.CharField(blank=True, max_length=255)
    contract_value = models.IntegerField(null=True)
    status_levy_payment = models.CharField(blank=True, max_length=255)
    architect_firm = models.CharField(blank=True, max_length=255)
    structural_civil_firm = models.CharField(blank=True, max_length=255)
    me_firm = models.CharField(blank=True, max_length=255)
    architect_firm = models.CharField(blank=True, max_length=255)
    gfa = models.FloatField(null=True)


    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name        



class Developer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    address1 = models.CharField(blank=True, max_length=255)
    address2 = models.CharField(blank=True, max_length=255)
    postcode = models.IntegerField(null=True)

    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)

    registration_number = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name    


class Contractor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    address1 = models.CharField(blank=True, max_length=255)
    address2 = models.CharField(blank=True, max_length=255)
    postcode = models.IntegerField(null=True)

    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(blank=True, max_length=255)

    cidb_reference_number = models.CharField(blank=True, max_length=255)
    cidb_registration_number = models.CharField(blank=True, max_length=255)
    cidb_registration_grade = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name    


class Representative(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=False, max_length=255)

    REPRESENTATIVE_TYPE = [
        ('CN', 'Contractor'),   
        ('DE', 'Developer'),   

        ('NA', 'Not Available'),   
    ]

    representative_type = models.CharField(
        max_length=2,
        choices=REPRESENTATIVE_TYPE,
        default='NA',
    )    

    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)

    position = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.name                  