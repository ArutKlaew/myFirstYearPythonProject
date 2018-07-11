from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    address = models.TextField(max_length=256)
    subdistrict = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    province = models.CharField(max_length=256)

    def __str__(self):
        return str(self.user) + " : address" + ("\n%s\n%s\n%s\n%s\n" % (self.address,self.subdistrict,self.district,self.province))


