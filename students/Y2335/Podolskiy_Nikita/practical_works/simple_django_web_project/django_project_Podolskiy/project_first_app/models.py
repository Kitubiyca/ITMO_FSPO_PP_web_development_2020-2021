from django.db import models


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    state_num = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(null=True, max_length=30)


class Owner(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthdate = models.DateField(null=True)


class Ownership(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class License(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    num = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    issue_date = models.DateField()
