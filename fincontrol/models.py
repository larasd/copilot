from django.db import models
import time
year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())

scenario_status_options= [
    ("S","Simulation"),
    ("E", "Efective"),
]
class Scenario:
    name=models.CharField(max_length=100)
    description=models.TexField()
    year=models.IntegerField(default=year)
    period=models.CharField(max_length=3)
    status=models.TexField(choices=scenario_status_options)
    version=models.IntegerField()



class ActivityType(models.Model):
    at = models.CharField(max_length=6)
    value = models.DecimalField(decimal_places=2)

class Resource(models.Model):
    scenario=models.ForeignKey(Scenario,on_delete=)
    name= models.CharField(max_lengt=100)
    third = models.BooleanField(default=False)
    at=models.ForeignKey(Scenario,on_delete=)





class Status(models.Model):
    status=models.CharField(max_length=20)

class Application(models.Model):
    apm_id=models.IntegerField()
    app_name=models.CharField(max_length=30)

account_options = [
    ("AO","Application Operation"),
    ("MA","Maintanance"),
    ("TU", "Technical upgrade"),

]
class Wbs(models.Model):
    wbs=models.CharField(max_length=15)
    account=models.CharField(choices=account_options)

class Periods(models.Model):
    week=models.IntegerField()
    period=models.IntegerField()

class Allocation(models.Model):
    resource=models.ForeignKey(Resource,on_delete=)
    rt=models.DecimalField(decimal_places=2)
    ot = models.DecimalField(decimal_places=2)


day_type_otions = [
    ('W', 'Weekend'),
    ('R', 'Regular'),
    ('H', 'Holiday'),
    ('V', 'Vacation'),
    ('A', 'Absence'),
]



class Calendar(models.Model):
    resource=models.ForeignKey(Resource,on_delete=)
    date=models.DateTimeField()
    day_type=models.CharField(max_length=20, choices=day_type_otions)



budget_type_otions = [
    ('Y', 'Yearly'),
    ('Q1', 'Q1 reviewed'),
    ('E', 'Expected'),
    ('A', 'Actuals'),
    ('J', 'Adjusted'),
    ('D','Delta')
]
class Budget(models.Model):
    budget_type=models.CharField(max_length=20, choices=budget_type_otions)

class BudgetDetails(models.Model):
    budget= models.ForeignKey(Budget, on_delete=)
    wbs=
    p1 = models.DecimalField(decimal_places=2, max_digits=12)
    p2 = models.DecimalField(decimal_places=2, max_digits=12)
    p3 = models.DecimalField(decimal_places=2, max_digits=12)
    p4 = models.DecimalField(decimal_places=2, max_digits=12)
    p5 = models.DecimalField(decimal_places=2, max_digits=12)
    p6 = models.DecimalField(decimal_places=2, max_digits=12)
    p7 = models.DecimalField(decimal_places=2, max_digits=12)
    p8 = models.DecimalField(decimal_places=2, max_digits=12)
    p9 = models.DecimalField(decimal_places=2, max_digits=12)
    p10 = models.DecimalField(decimal_places=2, max_digits=12)
    p11 = models.DecimalField(decimal_places=2, max_digits=12)
    p12 = models.DecimalField(decimal_places=2, max_digits=12)

