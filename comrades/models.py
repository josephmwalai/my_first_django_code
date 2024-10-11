from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Comrades(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    semester =models.IntegerField()
    academic_year = models.IntegerField()
    course = models.CharField(max_length=255)
    year_in_school = models.CharField(max_length=20, choices=YearInSchool,default=YearInSchool.FRESHMAN)

    def is_upperclas(self):
        return self.year_in_school in {
            self.YearInSchool.JUNIOR,
            self.YearInSchool.SENIOR
        }
