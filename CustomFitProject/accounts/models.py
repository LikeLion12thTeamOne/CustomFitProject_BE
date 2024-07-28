from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg 
from customFit.models import RecommendedProduct

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    terms_accepted_1 = models.BooleanField(default=False)
    terms_accepted_2 = models.BooleanField(default=False)
    terms_accepted_optional = models.BooleanField(default=False)  # 선택적 동의 필드

    # 선택지 정의
    AGE_CHOICES = [
        ('under_19', '19세 이하'),
        ('20-29', '20~29세'),
        ('30-39', '30~39세'),
        ('40-49', '40~49세'),
        ('50-59', '50~59세'),
        ('60-69', '60~69세'),
        ('over_70', '70 이상')
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    
    DISEASE_CHOICES = [
        ('diabetes', '당뇨'),
        ('muscle_loss', '근손실'),
        ('obesity', '비만'),
        ('hypertension', '고혈압')
    ]
    
    HEIGHT_CHOICES = [
        ('under_149', '149 cm 이하'),
        ('150-154', '150~154 cm'),
        ('155-159', '155~159 cm'),
        ('160-164', '160~164 cm'),
        ('165-169', '165~169 cm'),
        ('170-174', '170~174 cm'),
        ('175-179', '175~179 cm'),
        ('over_180', '180 cm 이상')
    ]
    
    WEIGHT_CHOICES = [
        ('under_39', '39kg 이하'),
        ('40-44', '40~44kg'),
        ('45-49', '45~49kg'),
        ('50-54', '50~54kg'),
        ('55-59', '55~59kg'),
        ('60-64', '60~64kg'),
        ('65-69', '65~69kg'),
        ('70-74', '70~74kg'),
        ('75-79', '75~79kg'),
        ('80-84', '80~84kg'),
        ('85-89', '85~89kg'),
        ('90-94', '90~94kg'),
        ('95-99', '95~99kg'),
        ('over_100', '100kg 이상')
    ]

    # 키워드 
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    age = models.CharField(max_length=100, choices=AGE_CHOICES, null=True)
    disease = models.CharField(max_length=100, choices=DISEASE_CHOICES, null=True, blank=True)
    height = models.CharField(max_length=100, choices=HEIGHT_CHOICES, null=True)
    weight = models.CharField(max_length=100, choices=WEIGHT_CHOICES, null=True)

    # 별점
    average_rating = models.FloatField(null=True, blank=True)

    def update_average_rating(self):
        self.average_rating = RecommendedProduct.objects.filter(user=self).aggregate(Avg('rating'))['rating__avg']
        self.save()


    def __str__(self):
        return self.username  
