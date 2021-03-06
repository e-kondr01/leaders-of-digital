from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timezone


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
    title = models.CharField(max_length=128)
    latitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    longitude = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    object = models.ForeignKey(Object, on_delete=models.PROTECT,
                               related_name='subobjects')

    def __str__(self) -> str:
        return f'{self.title}'


class Order(models.Model):
    order_num = models.CharField(max_length=16, null=True, verbose_name='Номер распоряжения')
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT,
                                     related_name='orders', null=True, verbose_name='Организация')
    subdivision = models.ForeignKey(Subdivision, on_delete=models.PROTECT,
                                    related_name='orders', null=True, verbose_name='Подразделение')
    object = models.ForeignKey(Object, on_delete=models.PROTECT,
                               related_name='orders', null=True, verbose_name='Место и наименование проведения работ')
    safety_desc = models.CharField(max_length=1024, null=True, verbose_name='Технические мероприятия по обеспечению безопасности работ')
    active = models.BooleanField(default=True, verbose_name='В процессе выполнения')

    instructions_given = models.BigIntegerField(null=True)
    instructions_received = models.BigIntegerField(null=True)
    job_started = models.BigIntegerField(null=True)
    job_finished = models.BigIntegerField(null=True)

    master = models.ForeignKey(Worker, on_delete=models.PROTECT,
                               related_name='given_orders', null=True)
    electrician = models.ManyToManyField(Worker, related_name='received_orders',
                                         verbose_name='Члены бригады')

    def __str__(self) -> str:
        return f'Распоряжение номер {self.order_num} от {self.master}'

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})

    def electricians(self):
        return self.electrician.all()

    def instructions_given_dt(self):
        if self.instructions_given:
            if len(str(self.instructions_given)) == 13:
                self.instructions_given //= 1000
            return datetime.fromtimestamp(self.instructions_given, timezone.utc)
        else:
            return 'Ещё нет'

    def instructions_received_dt(self):
        if self.instructions_received:
            if len(str(self.instructions_received)) == 13:
                self.instructions_received //= 1000
            return datetime.fromtimestamp(self.instructions_received, timezone.utc)
        else:
            return 'Ещё нет'

    def job_started_dt(self):
        if self.job_started:
            if len(str(self.job_started)) == 13:
                self.job_started //= 1000
            return datetime.fromtimestamp(self.job_started, timezone.utc)
        else:
            return 'Ещё нет'

    def job_finished_dt(self):
        if self.job_finished:
            if len(str(self.job_finished)) == 13:
                self.job_finished //= 1000
            return datetime.fromtimestamp(self.job_finished, timezone.utc)
        else:
            return 'Ещё нет'


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
    elimination_time = models.BigIntegerField(null=True)


class Report(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT,
                              related_name='reports')
    formed_at = models.BigIntegerField(null=True)
    received_at = models.BigIntegerField(null=True)
    received_by = models.ForeignKey(Worker, on_delete=models.PROTECT,
                               related_name='received_reports', null=True)

    def received_at_dt(self):
        if self.received_at:
            if len(str(self.received_at)) == 13:
                self.received_at //= 1000
            return datetime.fromtimestamp(self.received_at, timezone.utc)
        else:
            return 'Ещё не принято'

    def formed_at_dt(self):
        if self.formed_at:
            if len(str(self.formed_at)) == 13:
                self.formed_at //= 1000
            return datetime.fromtimestamp(self.formed_at, timezone.utc)
        else:
            return 'Нет времени осмотра'

    def __str__(self) -> str:
        return f'Листок осмотра {self.order}'

    def defects(self):
        return Defect.objects.filter(order=self.order).all()
