from django.db import models
import uuid


# Create your models here.
class Employee(models.Model):
    ID = models.UUIDField(default=uuid.uuid1(), max_length=50, primary_key=True)


class SystemUsersEN(models.Model):
    ID = models.CharField(max_length=50, default=uuid.uuid1())
    EmployeeUID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=100, primary_key=True, null=False)
