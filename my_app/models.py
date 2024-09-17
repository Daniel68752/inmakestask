from django.db import models

# Create your models here.
class Portfolio(models.Model):
    Full_name=models.CharField(max_length=200)
    Birthdate=models.DateField()
    Email=models.CharField(max_length=200)
    Phone=models.IntegerField()
    Skype=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.Full_name)

class Portfolio2(models.Model):
    Experience_present=models.CharField(max_length=500)
    Role=models.CharField(max_length=200)
    Designation=models.CharField(max_length=200)
    Exp_past=models.CharField(max_length=200)
    Role_past=models.CharField(max_length=200)
    Designation_past=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.Experience_present)

class PortfolioEdu(models.Model):
    br_year = models.CharField(max_length=200)
    Bachelor=models.CharField(max_length=200)
    Bachelor_college=models.CharField(max_length=200)
    pl_year = models.CharField(max_length=200)
    Plustwo=models.CharField(max_length=200)
    Plustwo_school=models.CharField(max_length=200)
    hs_year = models.CharField(max_length=200)
    Highschool=models.CharField(max_length=200)
    high_school=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.Bachelor)
