from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class SafetyGroup(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    safety_group = models.ForeignKey(SafetyGroup, on_delete=models.PROTECT,
                                     related_name='workers')
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.name} {self.safety_group}'


class Organization(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Subdivision(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title


class Object(models.Model):
    title = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Subobject(models.Model):
    title = models.CharField(max_length=32)
    object = models.ForeignKey(Object, on_delete=models.PROTECT,
                               related_name='subobjects')

    def __str__(self) -> str:
        return f'{self.title}'


class Order(models.Model):
    order_num = models.CharField(max_length=16, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     related_name='orders', null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.PROTECT,
                                    related_name='orders', null=True)
    object = models.ForeignKey(Object, on_delete=models.PROTECT,
                               related_name='orders', null=True)
    safety_desc = models.CharField(max_length=1024, null=True)
    active = models.BooleanField(default=True)
    instructions_given = models.DateTimeField(null=True)
    instructions_received = models.DateTimeField(null=True)
    job_started =  models.DateTimeField(null=True)
    job_finished = models.DateTimeField(null=True)
    master = models.ForeignKey(Worker, on_delete=models.PROTECT,
                               related_name='given_orders', null=True)
    electrician = models.ForeignKey(Worker, on_delete=models.PROTECT,
                                    related_name='received_orders', null=True)

    def __str__(self) -> str:
        return f'Распоряжение номер {self.order_num} от {self.master}'

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})


class DefectType(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title


class Defect(models.Model):
    subobject = models.ForeignKey(Subobject, on_delete=models.PROTECT,
                                  related_name='defects')
    order = models.ForeignKey(Order, on_delete=models.PROTECT,
                              related_name='defects')
    defect_type = models.ForeignKey(DefectType, on_delete=models.PROTECT,
                                    related_name='defects', null=True)
