import uuid
from django.db import models
from django.conf import settings


class Bills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100 , verbose_name='Bill Name')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name + " by " + str(self.user)

    def __unicode__(self):
        return unicode(self.name)


class BillsItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=250)
    price = models.FloatField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    negative = models.BooleanField(default=False)
    bill = models.ForeignKey(Bills ,null=True ,on_delete=models.CASCADE, related_name='bills')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.item + " - " + str(self.bill)
