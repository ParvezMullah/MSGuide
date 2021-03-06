from django.db import models
from django.utils.text import slugify

# Create your models here.


class UserProfile(models.Model):

    degree = (
        ('be', 'Bachelor of Engineering'),
        ('btech', 'Bachelor of Technology'),
        ('bsc', 'Bachelor of Science'),
    )
    country = (
        ('all', 'all'),
        ('United States', 'United States '),
        ('United Kingdom', 'United Kingdom'),
        ('Switzerland', 'Switzerland'),
        ('Singapore', 'Singapore'),
        ('Canada', 'Canada'),
        ('Netherland', 'Netherland')
    )

    full_name = models.CharField(
        max_length=50, help_text="sirname + first + last")
    education = models.CharField(choices=degree, max_length=40)
    graduation_CGPA = models.DecimalField(
        max_digits=4, decimal_places=3, help_text='Decimal upto 3')
    toefl = models.IntegerField(verbose_name="TOEFL", null=True, blank=True)
    gre_writing = models.DecimalField(max_digits=2, decimal_places=1,
                                      verbose_name="GRE writing", null=True, blank=True)
    gre_verbal = models.IntegerField(
        verbose_name="GRE Verbal", null=True, blank=True)
    gre_quantitative = models.IntegerField(
        verbose_name="GRE Quantitative", null=True, blank=True)
    gre_percentile = models.IntegerField(null=True, blank=True)
    work_experience = models.IntegerField(
        help_text='In years', default=0)
    Budget = models.IntegerField(help_text='In Lacs')
    email = models.EmailField(
        default='2016preeti.singh@ves.ac.in', max_length=254, editable=False)
    preferred_country = models.CharField(
        choices=country, max_length=40, default='all')

    def __str__(self):
        return self.full_name


class University(models.Model):
    University = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    fees_in_lakhs = models.IntegerField()
    gre_verbal = models.IntegerField()
    gre_writing = models.IntegerField()
    gre_quantitative = models.IntegerField()
    gre_percentile = models.IntegerField()
    toefl = models.IntegerField()
    overall_rating = models.IntegerField()
    grade = models.CharField(max_length=50)

    class Meta:
        db_table = 'university'

    def __str__(self):
        return self.University
