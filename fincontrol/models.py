from django.db import models

class ActivityType(models.Model):
    at = models.CharField(max_length=6)
    value = models.DecimalField(decimal_places=2)

class Status(models.Model):
    status=models.CharField(max_length=20)

class Application(models.Model):
    apm_id=models.IntegerField()
    app_name=models.CharField(max_length=30)

class Wbs(models.Model):
    wbs=models.CharField(max_length=15)

class Periods(models.Model):
    week=models.IntegerField()
    period=models.IntegerField()

class Allocation(models.Model):
    resource=
    rt=models.DecimalField(decimal_places=2)
    ot = models.DecimalField(decimal_places=2)


day_type_otions = [
    ('W', 'Weekend'),
    ('R', 'Regular'),
    ('H', 'Holiday'),
    ('V', 'Vacation'),
    ('A', 'Absence'),
]
class DayType(models.Model):
    day_type=

class Holidays(models.Model):

class Calendar(models.Model):
    resource=
    date=
    day_type=

budget_type_otions = [
    ('Y', 'Yearly'),
    ('Q1', 'Q1 reviewed'),
    ('E', 'Expected'),
    ('A', 'Actuals'),
    ('J', 'Adjusted'),
    ('D','Delta')
]
class Budget(models.Model):
    budget_type=

class Scenario:
    name=
    description=
    year=
    period=
    status=

