from django.db import models
from django.urls import reverse


# Create your models here.
class Order(models.Model):
    place = models.CharField(max_length=512)
    safety_desc = models.CharField(max_length=1024)
    '''
    master = models.ForeignKey(Master, on_delete=models.PROTECT,
                               related_name='given_orders')
    electrician = models.ForeignKey(Electrician, on_delete=models.PROTECT,
                                    related_name='received_orders')
    '''

    def __str__(self) -> str:
        return self.place

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})
